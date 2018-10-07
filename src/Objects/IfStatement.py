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
from src.Objects.builtinfuncs import *

class IfStatement():
    def __init__(self, line, variables):
        line = line.replace("(","")
        self.condition = line.replace(")","")
        self.variables = variables

        if "==" in self.condition:
            self.type = "equal"
            self.value1, self.value2 = self.condition.split("==")
        elif "in" in self.condition:
            self.type = "contain"
            self.value1, self.value2 = self.condition.split("in")
        elif "!=" in self.condition:
            self.type = "!equal"
            self.value1, self.value2 = self.condition.split("!=")
        else:
            self.type = None
            return

        if self.value1 in self.variables:
            self.value1 = str(self.variables[self.value1])
            self.value2 = self.value2.replace('"','')

        if self.value2 in self.variables:
            self.value1 = self.value1.replace('"','')
            self.value2 = str(self.variables[self.value2])

        else:
            self.value1 = self.value1.replace('"','')
            self.value2 = self.value2.replace('"','')


    def is_invalid(self):
        if self.type is None:
            return True

    def is_condition_true(self):
        if self.type == "equal":
            if self.value1 == self.value2:
                return True
        elif self.type == "contain":
            if self.value1 in self.value2:
                return True
        elif self.type == "!equal":
            if self.value1 != self.value2:
                return True
        return False


class ExecuteIfStatement():
    def __init__(self, file_name, line_number, line, e, variables):
        self.file_name = file_name
        self.line_number = line_number
        self.line = line
        self.display_error = e
        self.variables = variables

    def enter(self):
        self.line = self.line.replace("if","")
        self.line = self.line.replace(" ","")
        self.line = self.line.replace("{","")

        if "(" and ")" not in self.line:
            self.display_error.if_missing_bracket()

        if_statement = IfStatement(self.line, self.variables)

        if if_statement.is_invalid():
            self.display_error.if_invalid_token(); quit()
        elif if_statement.is_condition_true():
            return True
        else:
            return False

    def execute(self):
        self.line = self.line.replace("    ","")
        print_print(self.file_name, self.line_number, self.line, self.variables)
