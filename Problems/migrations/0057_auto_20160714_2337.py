# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-15 03:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0056_auto_20160714_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 22, 3, 37, 22, 451028, tzinfo=utc), null=True),
        ),
    ]