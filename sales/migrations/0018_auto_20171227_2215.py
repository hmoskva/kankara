# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0017_auto_20171227_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.CharField(blank=True, choices=[('kankara', 'Kankara'), ('small drink', 'Small Drink'), ('big drink', 'Big Drink'), ('mtn card', 'MTN Card'), ('glo card', 'Glo Card'), ('9mobile card', '9Mobile Card'), ('airtel card', 'Airtel Card')], max_length=120, null=True),
        ),
    ]