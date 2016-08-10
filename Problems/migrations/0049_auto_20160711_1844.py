# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-11 22:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0048_auto_20160709_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='markedquestion',
            name='answer',
            field=models.TextField(default='', verbose_name=b'Answer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 18, 22, 44, 10, 285324, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='expires',
            field=models.DateTimeField(verbose_name=b'Expires on'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='live',
            field=models.DateTimeField(verbose_name=b'Live on'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='out_of',
            field=models.IntegerField(default=1, verbose_name=b'Points'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='tries',
            field=models.IntegerField(default=0, verbose_name=b'Tries'),
        ),
        migrations.AlterField(
            model_name='studentquizresult',
            name='attempt',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='studentquizresult',
            name='cur_quest',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='studentquizresult',
            name='result',
            field=models.TextField(default=b'{}'),
        ),
    ]