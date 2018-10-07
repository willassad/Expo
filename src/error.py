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


class DisplayError():
    def __init__(self,line_number,file_name):
        self.line_number = line_number
        self.file_name = file_name

    def show_error(self,message):
        default_message = "ERROR: line %s in %s." %(self.line_number,self.file_name)
        print(default_message+"\n"+message); quit()

    def var_not_integer(self, var):
        self.show_error("Value '%s' must be integer." %var)

    def var_not_string(self, var):
        self.show_error("Value '%s' must be string." %var)

    def not_string(self):
        self.show_error("Value must be string.")

    def var_not_boolean(self, var):
        self.show_error("Value '%s' must be boolean." %var)

    def var_not_defined(self, var):
        self.show_error("Variable '%s' is not defined." %var)

    def if_missing_bracket(self):
        self.show_error("Invalid syntax missing parentheses ()")

    def if_invalid_token(self):
        self.show_error("Unknown token.")

    def repeat_not_int(self, var):
        self.show_error("Variable '%s' does not contain an integer." %var)

    def missing_statement_end(self):
        self.show_error("Invalid syntax missing ';'")

    def invalid_syntax(self):
        self.show_error("Invalid Syntax")

    def general_error():
        print("ERROR")
