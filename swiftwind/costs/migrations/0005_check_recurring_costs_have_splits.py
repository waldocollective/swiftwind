# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0004_check_total_billing_cycles_over_zero'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION check_recurring_costs_have_splits()
                RETURNS trigger AS
            $$
            DECLARE
                total_splits INT;
            BEGIN
                SELECT INTO total_splits COUNT(*) FROM costs_recurringcostsplit WHERE recurring_cost_id = NEW.id;

                IF total_splits = 0 THEN
                    RAISE EXCEPTION 'Recurring costs must be created with splits.'
                        USING ERRCODE = 'integrity_constraint_violation';
                END IF;
                RETURN NEW;
            END;
            $$
            LANGUAGE plpgsql;
            """,
            "DROP FUNCTION check_recurring_costs_have_splits()"
        ),
        migrations.RunSQL(
            """
            CREATE CONSTRAINT TRIGGER check_recurring_costs_have_splits_trigger
            AFTER INSERT ON costs_recurringcost
            DEFERRABLE INITIALLY DEFERRED
            FOR EACH ROW EXECUTE PROCEDURE check_recurring_costs_have_splits()
            """,
            "DROP TRIGGER check_recurring_costs_have_splits_trigger ON costs_recurringcost"
        )
    ]
