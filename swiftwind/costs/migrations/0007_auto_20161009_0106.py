# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0006_auto_20161009_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringcost',
            name='fixed_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
    ]
