# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20171227_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount_paid',
            field=models.IntegerField(default=0, verbose_name='Amount Paid'),
        ),
    ]
