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
from django.db import IntegrityError

@csrf_exempt
def log(request):
    logger.debug(request.POST)
    resp = dict() #request.POST)   # 必须新建一个dict，否则无法修改

    e = Employee.objects.get(name_text = request.POST['employee'])
    u = request.POST['ucode']
    r = Record()
    r.ucode_text = u
    r.employee = e
    r.datetime = datetime.now()
    try:
        r.save()
    except IntegrityError:
        resp['error'] = "duplicated entry"
        r = Record.objects.get(ucode_text = u)
        resp['e-employee'] = r.employee.name_text
        resp['e-datetime'] = r.datetime
    else:
        resp['ucode']     = u
       # resp['employee'] = e
        resp['datetime'] = datetime.now()

    return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder), content_type="application/json")
    #return HttpResponse(request.POST['ucode'])

def records(request):
    eName = request.GET['employee']
    e = Employee.objects.get(name_text = eName)
    rs = e.record_set.all()
    a = []
    for r in rs:
        a.append({"ucode": r.ucode_text,
                  "datetime": r.datetime})
    logger.debug(a)

    return HttpResponse(json.dumps(a, cls=DjangoJSONEncoder), content_type="application/json")