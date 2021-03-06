from datetime import date

from django.core.management.base import BaseCommand

from swiftwind.billing_cycle.models import BillingCycle


class Command(BaseCommand):
    help = 'Enact any costs which need to be enacted'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--as_of',
            action='store',
            dest='as_of',
            default=None,
            help="Enact for billing cycles up until this date, in format YYYY-MM-DD. Defaults to today's date.",
        )

    def handle(self, *args, **options):
        if options.get('as_of'):
            as_of = date(*map(int, options['as_of'].split('-')))
        else:
            as_of = date.today()
        for billing_cycle in BillingCycle.objects.filter(start_date__lt=as_of, transactions_created=False):
            billing_cycle.enact_all_costs()
