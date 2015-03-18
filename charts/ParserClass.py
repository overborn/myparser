# -*- coding: utf-8 -*-
from charts.models import Entry
import json
import xlrd

import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts)
        return result

    return timed


class ParserCLass(object):
    def __init__(self, source):
        self.source = source

    def parse_and_save(self):
        raise NotImplementedError


class CSV_Parser(ParserCLass):
    @timeit
    def parse_and_save(self):
        with open(self.source.name) as f:
            f.readline()
            entries = []
            for line in f:
                e = Entry.create(*line.decode('utf-8').split(','))
                entries.append(e)
        Entry.objects.bulk_create(entries)


class JSON_Parser(ParserCLass):
    @timeit
    def parse_and_save(self):
        obj = json.load(self.source)
        entries = []
        for entry in obj['data']:
            e = Entry.create(entry[obj['structure'][0]],
                             entry[obj['structure'][1]],
                             entry[obj['structure'][2]])
            entries.append(e)
        Entry.objects.bulk_create(entries)


class XLS_Parser(ParserCLass):
    @timeit
    def parse_and_save(self):
        book = xlrd.open_workbook(self.source.name)
        sheet = book.sheet_by_index(0)
        entries = []
        for rownum in range(1, sheet.nrows):
            e = Entry.create(*sheet.row_values(rownum))
            entries.append(e)
        Entry.objects.bulk_create(entries)
