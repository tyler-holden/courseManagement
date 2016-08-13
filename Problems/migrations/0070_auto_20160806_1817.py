# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-06 22:17
from __future__ import unicode_literals

import Problems.models
import Problems.validators
import datetime
import django.core.files.storage
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0069_auto_20160806_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='expires',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 8, 13, 22, 17, 6, 97872, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='doc_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/tholden/djangotest/course_website/notes'), upload_to=Problems.models.note_name_setter, validators=[Problems.validators.FileValidator(content_types=('application/pdf', 'image/jpeg', 'image/png'), max_size=512000)]),
        ),
    ]
