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


def get_source(file_name):
    # Open source code file and get it's content and save it to the 'contents' var
    try:
        source = open(file_name,"r")
    except Exception:
        print("ERROR: File %s cannot be found." %file_name)
        source = []

    code = []
    original_code = []
    for s in source:
        s = s.strip("\n")
        original_code.append(s)
        if s[:2]=="//":
            pass
        else:
            if s != "":
                code.append(s)

    return [code,original_code]

def code(file_name):
    source = get_source(file_name)
    code = source[0]
    return code

def original_code(file_name):
    source = get_source(file_name)
    code = source[1]
    return code
