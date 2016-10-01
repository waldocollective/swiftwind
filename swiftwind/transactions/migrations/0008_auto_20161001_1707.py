# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_transactionimport_hordak_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionimport',
            name='date_format',
            field=models.CharField(choices=[('%d-%m-%Y', 'dd-mm-yyyy'), ('%d/%m/%Y', 'dd/mm/yyyy'), ('%d.%m.%Y', 'dd.mm.yyyy'), ('%d-%Y-%m', 'dd-yyyy-mm'), ('%d/%Y/%m', 'dd/yyyy/mm'), ('%d.%Y.%m', 'dd.yyyy.mm'), ('%m-%d-%Y', 'mm-dd-yyyy'), ('%m/%d/%Y', 'mm/dd/yyyy'), ('%m.%d.%Y', 'mm.dd.yyyy'), ('%m-%Y-%d', 'mm-yyyy-dd'), ('%m/%Y/%d', 'mm/yyyy/dd'), ('%m.%Y.%d', 'mm.yyyy.dd'), ('%Y-%d-%m', 'yyyy-dd-mm'), ('%Y/%d/%m', 'yyyy/dd/mm'), ('%Y.%d.%m', 'yyyy.dd.mm'), ('%Y-%m-%d', 'yyyy-mm-dd'), ('%Y/%m/%d', 'yyyy/mm/dd'), ('%Y.%m.%d', 'yyyy.mm.dd'), ('%d-%m-%y', 'dd-mm-yy'), ('%d/%m/%y', 'dd/mm/yy'), ('%d.%m.%y', 'dd.mm.yy'), ('%d-%y-%m', 'dd-yy-mm'), ('%d/%y/%m', 'dd/yy/mm'), ('%d.%y.%m', 'dd.yy.mm'), ('%m-%d-%y', 'mm-dd-yy'), ('%m/%d/%y', 'mm/dd/yy'), ('%m.%d.%y', 'mm.dd.yy'), ('%m-%y-%d', 'mm-yy-dd'), ('%m/%y/%d', 'mm/yy/dd'), ('%m.%y.%d', 'mm.yy.dd'), ('%y-%d-%m', 'yy-dd-mm'), ('%y/%d/%m', 'yy/dd/mm'), ('%y.%d.%m', 'yy.dd.mm'), ('%y-%m-%d', 'yy-mm-dd'), ('%y/%m/%d', 'yy/mm/dd'), ('%y.%m.%d', 'yy.mm.dd')], default='%d-%m-%Y', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactionimportcolumn',
            name='to_field',
            field=models.CharField(blank=True, choices=[(None, '-- Do not import --'), ('date', 'Date'), ('amount', 'Amount'), ('amount_out', 'Amount (money in only)'), ('amount_in', 'Amount (money out only)'), ('description', 'Description / Notes')], default=None, max_length=20, null=True, verbose_name='Is'),
        ),
    ]
