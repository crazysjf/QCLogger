# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import logging
logger = logging.getLogger("django")

from django.http import HttpResponse

# Create your views here.
from .models import Employee, Record
def index(request):
    employees = Employee.objects.all()
    # output = ', '.join([e.name_text for e in employees])
    # return HttpResponse(output)
    #
    # = get_object_or_404(Question, pk=question_id)
    logger.debug('viewing index')

    return render(request, 'QCLoggerApp/index.html', {'employees': employees})

def log(request):
    logger.debug(request.POST)
    return HttpResponse(request.POST['ucode'])
