# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QCLoggerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(db_index=True, verbose_name='registering date'),
        ),
        migrations.AlterField(
            model_name='record',
            name='ucode_text',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]