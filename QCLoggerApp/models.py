# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    name_text = models.CharField(max_length=200)
    reg_date = models.DateTimeField('registering date') # 注册日期

    def __str__(self):
        return self.name_text

class Record(models.Model):
    employee = models.ForeignKey(Employee)
    ucode_text = models.CharField(max_length=200) # 唯一码
    date = models.DateTimeField('registering date')

    def __str__(self):
        return self.ucode_text
