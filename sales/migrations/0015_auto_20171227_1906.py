# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_auto_20171227_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
