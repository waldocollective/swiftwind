from dateutil.relativedelta import relativedelta
from django.contrib.postgres.fields import DateRangeField
from django.db import models
from django.db import transaction as db_transaction
from django.db.models.functions import Lower, Upper
from django.utils.datetime_safe import datetime, date
from django_smalluuid.models import uuid_default, SmallUUIDField
from django.conf import settings

from .cycles import get_billing_cycle


class BillingCycleManager(models.Manager):

    def get_queryset(self):
        queryset = super(BillingCycleManager, self).get_queryset()
        return queryset\
            .annotate(start_date=Lower('date_range'))\
            .annotate(end_date=Upper('date_range'))

    def enactable(self, as_of):
        """Find all billing cycles that should be enacted

        This consists of any billing cycle that has not had transactions created
        for it, and has a start date prior to `as_of`.
        """
        return self.filter(
            transactions_created=False,
            start_date__lte=as_of,
        )


class BillingCycle(models.Model):
    uuid = SmallUUIDField(default=uuid_default(), editable=False)
    date_range = DateRangeField(
        help_text='The start and end date of this billing cycle. '
                  'May not overlay with any other billing cycles.'
    )
    transactions_created = models.BooleanField(
        default=False,
        help_text='Have transactions been created for this billing cycle?'
    )

    objects = BillingCycleManager()

    class Meta:
        ordering = ['date_range']

    def __str__(self):
        return 'BillingCycle <{}>'.format(self.date_range)

    @classmethod
    def populate(cls):
        """Ensure the next X years of billing cycles exist
        """
        return cls._populate(as_of=date.today(), delete=True)

    @classmethod
    def repopulate(cls):
        """Create the next X years of billing cycles

        Will delete any billing cycles which are in the future
        """
        return cls._populate(as_of=date.today(), delete=False)

    @classmethod
    def _populate(cls, as_of=None, delete=False):
        if as_of is None:
            as_of = datetime.now().date()

        billing_cycle = get_billing_cycle()
        stop_date = as_of + relativedelta(years=settings.SWIFTWIND_BILLING_CYCLE_YEARS)
        date_ranges = billing_cycle.generate_date_ranges(as_of, stop_date=stop_date)

        with db_transaction.atomic():

            if delete:
                # Delete all the future unused transactions
                cls.objects.filter(start_date__gt=as_of).delete()

            # Now recreate the upcoming billing cycles
            for start_date, end_date in date_ranges:
                if not delete:
                    exists = BillingCycle.objects.filter(date_range=[start_date, end_date]).count()
                    if exists:
                        # If we are not deleting (i.e. updating only), then don't
                        # create this BillingCycle if one already exists
                        continue

                BillingCycle.objects.create(
                    date_range=(start_date, end_date),
                )


