# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0004_auto_20160424_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='solved',
            field=models.IntegerField(default=0),
        ),
    ]
