# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-14 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0024_auto_20160513_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 6, 4, 19, 52, 7, 433924, tzinfo=utc), null=True),
        ),
    ]