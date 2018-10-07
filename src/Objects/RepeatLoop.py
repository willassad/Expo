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

class ExecuteRepeat():
    def __init__(self, file_name, line_number, line, e, variables):
        self.file_name = file_name
        self.line_number = line_number
        self.line = line
        self.display_error = e
        self.variables = variables
        self.repeat = 0

    def enter(self):
        line = self.line.replace("repeat",""); line = line.replace(" ","")
        line = line.replace("(",""); line = line.replace(")","");
        self.line = line.replace("{","")

        try:
            self.repeat = int(self.line)
        except Exception as e:
            if self.line in self.variables:
                store = self.variables[self.line]
                if type(store) == int:
                    self.repeat = int(store)
                else:
                    self.display_error.var_not_integer(self.line); quit()
            else:
                self.display_error.var_not_defined(self.line); quit()

        if self.repeat > 0:
            return [True, self.repeat]
        else:
            return [False, self.repeat]

    def execute(self,repeat):
        self.line = self.line.replace("    ","")
        for x in range(0,repeat):
            print_print(self.file_name, self.line_number, self.line, self.variables)
