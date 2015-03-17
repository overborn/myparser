# -*- coding: utf-8 -*-
from charts.models import Entry
import json
import xlrd


class ParserCLass(object):
    def __init__(self, source):
        self.source = source

    def parse_and_save(self):
        raise NotImplementedError


class CSV_Parser(ParserCLass):
    def parse_and_save(self):
        with open(self.source.name) as f:
            f.readline()
            for line in f:
                e = Entry.create(*line.decode('utf-8').split(','))
                e.save()


class JSON_Parser(ParserCLass):
    def parse_and_save(self):
        obj = json.load(self.source)
        for entry in obj['data']:            
            e = Entry.create(entry[obj['structure'][0]],
                             entry[obj['structure'][1]],
                             entry[obj['structure'][2]])
            e.save()


class XLS_Parser(ParserCLass):
    def parse_and_save(self):
        book = xlrd.open_workbook(self.source.name)
        sheet = book.sheet_by_index(0)
        for rownum in range(1, sheet.nrows):
            e = Entry.create(*sheet.row_values(rownum))
            e.save()
