# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0002_auto_20170910_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvbackup',
            name='upload_by',
            field=models.CharField(blank=True, choices=[('UN', 'UTORid'), ('SN', 'Student Number')], max_length=2, null=True),
        ),
    ]
