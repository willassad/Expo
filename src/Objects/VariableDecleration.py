#!/usr/bin/python
# -*- coding: utf-8 -*-
# Project File: Python 2.x or 3.x

__author__ = "Will Assad"
__copyright__ = "Copyright 2018, EXPO"
__credits__ = ["Will Assad"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Will Assad"
__email__ = "willassadcode@gmail.com"
__status__ = "Production"

#IMPORTS
import ast

class DeclareVariable():
    def __init__(self, file_name, line_number, line, e):
        self.file_name = file_name
        self.line_number = line_number
        self.line = line
        self.display_error = e

    def declare_int(self):
        line = self.line.replace("int",""); line = line.replace(" ",""); self.line = line.replace(";","")
        var = self.line[0:self.line.find("=")]; value = self.line[self.line.find("=")+1:]
        if not value.isdigit():
            self.display_error.var_not_integer(var); quit()
        else:
            return [var, int(value)]

    def declare_str(self):
        self.line = list(self.line.replace("str",""))

        try:
            for i in range(0,self.line.index('"')):
                self.line[i] = self.line[i].replace(" ","")
        except:
            self.display_error.not_string(); quit()

        self.line = ''.join(str(n) for n in self.line).replace(";","")
        var = self.line[0:self.line.find("=")]
        value = self.line[self.line.find("=")+1:]

        temp_value = list(value)
        for i in reversed(range(len(temp_value))):
            if temp_value[i] == '"': break
            else: temp_value[i] = temp_value[i].replace(" ","")

        value = ''.join(str(n) for n in temp_value)

        if (value[0] != '"' or value[-1] != '"'):
            self.display_error.var_not_string(var); quit()
        else:
            return [var, value.replace('"',"")]


    def declare_bool(self):
        self.line = list(self.line.replace("bool",""))
        for i in range(0,len(self.line)):
            self.line[i] = self.line[i].replace(" ","")

        self.line = ''.join(str(n) for n in self.line).replace(";","")
        var = self.line[0:self.line.find("=")]
        value = self.line[self.line.find("=")+1:]

        if value not in ['True','False','None']:
            self.display_error.var_not_boolean(var); quit()

        value = ast.literal_eval(value)
        return [var, value]
