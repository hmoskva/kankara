# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0016_auto_20171227_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='business_type',
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.CharField(choices=[('fully paid', 'Fully Paid'), ('partly paid', 'Partly Paid'), ('not paid', 'Awiin')], default='fully paid', max_length=120),
        ),
    ]