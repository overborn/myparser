# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from charts.forms import FileForm, ChartForm
from charts.ParserClass import CSV_Parser, JSON_Parser, XLS_Parser
from charts.models import Entry
import json


def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['source']
            if f.name.split('.')[-1] == 'csv':
                parser = CSV_Parser(f)
                parser.parse_and_save()
            elif f.name.split('.')[-1] == 'xls':
                parser = XLS_Parser(f)
                parser.parse_and_save()
            elif f.name.split('.')[-1] == 'json':
                parser = JSON_Parser(f)
                parser.parse_and_save()
            else:
                pass
        return HttpResponseRedirect('/charts')
    else:
        form = FileForm()
    context_dict = {'form': form}
    return render_to_response('index.html', context_dict, context)


def charts(request):
    context = RequestContext(request)
    regions = Entry.objects.values_list('region', flat=True).distinct()
    choices = [(reg, reg) for reg in regions]
    form = ChartForm(choices=choices)
    context_dict = {'form': form}
    return render_to_response('charts.html', context_dict, context)


def build_chart(request):
    if request.method == "GET":
        region = request.GET['region']
        data = {}
        entries = Entry.objects.filter(region=region)
        data['xAxis'] = [e.city for e in entries]
        data['yAxis'] = [e.value for e in entries]
        return HttpResponse(json.dumps(data), content_type="application/json")


def delete_entries(request):
    Entry.objects.all().delete()
    return HttpResponseRedirect('/index/')
