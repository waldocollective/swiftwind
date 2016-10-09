# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0010_auto_20161009_1225'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE costs_recurringcost ADD CONSTRAINT fixed_amount_requires_type_normal
            CHECK (
                ("type" = 'normal' AND fixed_amount IS NOT NULL)
                OR
                ("type" != 'normal' AND fixed_amount IS NULL)
            )
            """,
            "ALTER TABLE costs_recurringcost DROP CONSTRAINT fixed_amount_requires_type_normal"
        )
    ]