# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-30 19:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0009_auto_20160430_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 5, 21, 19, 53, 23, 179358, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='questionstatus',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='Problems.Question'),
        ),
    ]
