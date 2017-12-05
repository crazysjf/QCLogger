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

from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def log(request):
    logger.debug(request.POST)
    resp = dict(request.POST)   # 必须新建一个dict，否则无法修改
    resp['datetime'] = datetime.now()
    return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder), content_type="application/json")
    #return HttpResponse(request.POST['ucode'])
