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
from src.error import DisplayError

def print_print(file_name, line_number, line, variables):
    line = line.replace("print","")
    line = line.replace(" ","")
    to_print = line.replace(";","")
    e = DisplayError(line_number,file_name)

    try:

        if to_print[0]=='"' and to_print[-1]=='"':
            to_print = to_print.replace('"',"")
            print(to_print)
        else:
            try:
                print(variables[to_print])
            except:
                e.var_not_defined(to_print); quit()

    except IndexError:
        e.invalid_syntax(); quit()
