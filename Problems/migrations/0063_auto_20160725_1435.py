# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-25 18:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0062_auto_20160725_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 8, 1, 18, 35, 5, 779583, tzinfo=utc), null=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentvote',
            unique_together=set([('student', 'question', 'cur_poll')]),
        ),
    ]
