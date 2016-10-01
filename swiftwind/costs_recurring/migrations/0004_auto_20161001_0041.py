# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models


class Migration(migrations.Migration):

    dependencies = [
        ('costs_recurring', '0003_auto_20160930_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringcostsplit',
            name='uuid',
            field=django_smalluuid.models.SmallUUIDField(default=django_smalluuid.models.UUIDDefault(), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='recurringcostsplit',
            name='recurring_cost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splits', to='costs_recurring.RecurringCost'),
        ),
    ]