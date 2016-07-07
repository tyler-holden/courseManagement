# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 21:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0042_auto_20160707_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 14, 21, 10, 3, 280090, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='markedquestion',
            name='choices',
            field=models.TextField(null=True),
        ),
    ]
