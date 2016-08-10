# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-25 18:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0061_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 8, 1, 18, 25, 17, 909068, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='pollquestion',
            name='text',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]