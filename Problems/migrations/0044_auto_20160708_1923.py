# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-08 23:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0043_auto_20160708_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 29, 23, 23, 12, 926407, tzinfo=utc), null=True),
        ),
    ]