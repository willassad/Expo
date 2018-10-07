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
from src.Objects.builtinfuncs import *
from src.getsource import code as get_code
from src.getsource import original_code as get_original
from src.Objects.VariableDecleration import *
from src.Objects.IfStatement import *
from src.Objects.RepeatLoop import *

def execute_source_code(file_name):
    code = get_code(file_name)
    original_code = get_original(file_name)
    variables = {}

    enter_if = False
    enter_else = False
    enter_for = False

    for line in code:
        line_number = str(original_code.index(line)+1)
        display_error = DisplayError(line_number,file_name)

        var = DeclareVariable(file_name,line_number,line,display_error)
        if_st = ExecuteIfStatement(file_name,line_number,line,display_error,variables)
        repeat_loop = ExecuteRepeat(file_name,line_number,line,display_error,variables)

        if '}' not in line and '{' not in line:
            if line.replace(" ","")[-1] != ";":
                display_error.missing_statement_end(); break

        if line[:3] == "int":
            variable = var.declare_int()
            variables[variable[0]] = variable[1]

        elif line[:3] == "str":
            variable = var.declare_str()
            variables[variable[0]] = variable[1]

        elif line[:4] == "bool":
            variable = var.declare_bool()
            variables[variable[0]] = variable[1]

        elif line[:5] == "print":
            print_print(file_name, line_number, line, variables)

        elif line[:2] == "if":
            if_executed = False
            enter_if = if_st.enter()

        elif line[:4] == "    ":
            if enter_if:
                if_st.execute()
                if_executed = True
                enter_if = False
                enter_else = False
            elif enter_else and not if_executed:
                if_st.execute()
                enter_else = False
            elif enter_for:
                repeat_loop.execute(repeat[1])
                enter_for = False

        elif line.replace(" ","") == "}else{":
            if enter_if:
                enter_else = False
            else:
                enter_else = True

        elif line[:6] == "repeat":
            repeat = repeat_loop.enter()
            enter_for = repeat[0]
