# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(verbose_name='registering date')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ucode_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='registering date')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QCLoggerApp.Employee')),
            ],
        ),
    ]
