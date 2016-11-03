#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render

from rest_framework import status

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import(
        AllowAny,
        IsAuthenticated
)
from rest_framework.decorators import(
        api_view,
        permission_classes,
        parser_classes,
)
from .models import *

from table.views import FeedDataView

from app.tables import (
    ModelTable, AjaxTable, AjaxSourceTable,
    CalendarColumnTable, SequenceColumnTable,
    LinkColumnTable, CheckboxColumnTable
)

def base(request):
    table = ModelTable()
#    from django.http import HttpResponse
#    import json
#    json_tmp={'people':table}
#    return  HttpResponse(json.dumps(json_tmp))

    return render(request, "index.html", {'people': table})
#    return JsonResponse({'people': table})


@api_view(['GET'])
@permission_classes([AllowAny])
def bulks(request):
    bulk_list = []
    bulks = Bulk.objects.all()
    for x in bulks:
        bulk_id = x.id
        bulk_title = x.title
        bulk_reseller_mob = x.reseller_mob
        bulk_receive_mode = x.receive_mode
        bulk_start_time = x.start_time
        bulk_dead_time = x.dead_time
        bulk_status = x.status
        bulk_volume = x.volume
        bulk_details = x.details
        bulk_data ={
            'id':bulk_id,
            'title':bulk_title,
            'reseller_mob':bulk_reseller_mob,
            'receive_mode':bulk_receive_mode,
            'start_time':bulk_start_time,
            'dead_time':bulk_dead_time,
            'status':bulk_status,
            'volume':bulk_volume,
            'details':bulk_details
        }
        bulk_list.append(bulk_data)
    rst_data = {
        "data":bulk_list
    }
    return Response(rst_data,status=status.HTTP_200_OK)


def ajax(request):
    table = AjaxTable()
    return render(request, "index.html", {'people': table})


def ajax_source(request):
    table = AjaxSourceTable()
    return render(request, "index.html", {'people': table})


class Foo(object):
    def __init__(self, id, name, calendar):
        self.id = id
        self.name = name
        self.calendar = calendar


def sequence_column(request):
    data = [
        Foo(1, 'A', [1, 2, 3, 4, 5]),
        Foo(2, 'B', [1, 2, 3, 4, 5]),
        Foo(3, 'C', [1, 2, 3, 4, 5])
    ]
    table = SequenceColumnTable(data)
    return render(request, "index.html", {'people': table})


def calendar_column(request):
    data = [
        Foo(1, 'A', range(1, 14)),
        Foo(2, 'B', range(1, 14)),
        Foo(3, 'C', range(1, 14))
    ]
    table = CalendarColumnTable(data)
    return render(request, "index.html", {'people': table})


def link_column(request):
    table = LinkColumnTable()
    return render(request, "index.html", {'people': table})


def checkbox_column(request):
    table = CheckboxColumnTable()
    return render(request, "index.html", {'people': table})


def user_profile(request, uid):
    from app.models import Person
    from django.http import HttpResponse
    from django.shortcuts import get_object_or_404
    person = get_object_or_404(Person, pk=uid)
    return HttpResponse("User %s" % person.name)


class MyDataView(FeedDataView):

    token = AjaxSourceTable.token

    def get_queryset(self):
        return super(MyDataView, self).get_queryset().filter(id__gt=5)
