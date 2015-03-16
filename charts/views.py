# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from charts.forms import FileForm
from charts.ParserClass import CSV_Parser, JSON_Parser, XLS_Parser
from charts.models import Entry


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
    entries = Entry.objects.all()
    context_dict = {'entries': entries}
    return render_to_response('charts.html', context_dict, context)


def delete_entries(request):
    Entry.objects.all().delete()
    return HttpResponseRedirect('/index/')
