# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 17:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20171227_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2017, 12, 27, 17, 49, 45, 625218, tzinfo=utc)),
        ),
    ]
