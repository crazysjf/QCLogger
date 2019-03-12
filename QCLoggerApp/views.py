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

def reports(request):
    employees = Employee.objects.all()
    return render(request, 'QCLoggerApp/reports.html', {'employees': employees})

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
        # 格式和records返回格式保持一致方便前端处理
        resp['ucodeList']     = [u]
        resp['employeeList'] = [e.name_text]
        resp['datetimeList'] = [datetime.now()]

    return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder), content_type="application/json")
    #return HttpResponse(request.POST['ucode'])

from django.utils.timezone import now, timedelta
from datetime import datetime

# 返回用户的记录条数。如果没有指定时间，则时间为当天
def recordCount(request):
    eName           = request.GET.get('employee',False)
    uCode           = request.GET.get('ucode',False)
    datetimeStart   = request.GET.get('datetimeStart',False)
    datetimeEnd     = request.GET.get('datetimeEnd',False)

    if datetimeStart == False or datetimeEnd == False:
        datetimeStart = now().date()
        datetimeEnd = datetimeStart + timedelta(days=1)

    e = Employee.objects.get(name_text = eName)
    cnt = e.record_set.filter(datetime__range=(datetimeStart, datetimeEnd)).count()
    return HttpResponse(json.dumps({"recordCount":cnt}, cls=DjangoJSONEncoder), content_type="application/json")

def records(request):
    eName           = request.GET.get('employee',"")
    startDateStr       = request.GET.get('startDate', "")
    endDateStr         = request.GET.get('endDate', "")
    ucode           = request.GET.get('ucode', "")

    startDate = 0
    endDate = 0
    #e = Employee.objects.get(name_text = eName)
    if startDateStr == "" or endDateStr == "":
        startDate = now().date()
        endDate = startDate + timedelta(days=1)
    else:
        startDate = datetime.strptime(startDateStr, '%Y-%m-%d')
        endDate = datetime.strptime(endDateStr + " 23:59:59", '%Y-%m-%d %H:%M:%S')

    objs = Record.objects
    if ucode != "" :
        objs = objs.filter(ucode_text__exact = ucode)

    if eName != "":
        objs = objs.filter(employee__name_text = eName)

    rs = objs.filter(datetime__range=(startDate, endDate)).order_by("-datetime")

    #rs  = e.record_set.filter(datetime__range=(start, end)).order_by("-datetime")
    employeeList = []
    ucodeList = []
    datetimeList = []
    for r in rs:
        employeeList.append(r.employee.name_text)
        ucodeList.append(r.ucode_text)
        datetimeList.append(r.datetime)
    a = {}
    a['employeeList']   = employeeList
    a['ucodeList']       = ucodeList
    a['datetimeList']   = datetimeList

    return HttpResponse(json.dumps(a, cls=DjangoJSONEncoder), content_type="application/json")