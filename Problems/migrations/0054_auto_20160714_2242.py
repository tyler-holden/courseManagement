# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-15 02:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0053_auto_20160714_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 22, 2, 42, 26, 959481, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='markedquestion',
            name='functions',
            field=models.TextField(default='[]', verbose_name='Functions'),
        ),
        migrations.AlterField(
            model_name='markedquestion',
            name='mc_choices',
            field=models.TextField(default='{}', verbose_name='Multiple Choice'),
        ),
        migrations.AlterField(
            model_name='markedquestion',
            name='q_type',
            field=models.CharField(choices=[('D', 'Direct Entry'), ('MC', 'Multiple Choice'), ('TF', 'True/False')], default='D', max_length=2, verbose_name='Question Type'),
        ),
    ]