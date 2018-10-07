#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Project File: Python 2.x or 3.x

__author__ = "Will Assad"
__copyright__ = "Copyright 2018, Expo"
__credits__ = ["Will Assad"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Will Assad"
__email__ = "willassadcode@gmail.com"
__status__ = "Production"

#IMPORTS
import src.execute as execute
import os
import sys


def main():
    path = os.getcwd()

    try: 
        file_name = sys.argv[1]
    except:
        print("ERROR: Need File Name to be Run e.g 'exp main.expo'")
        return None

    if file_name[len(file_name) - 5:len(file_name)] != ".expo":
        print("ERROR: File extension not recognised.")
        return None

    try:
        print('ERROR: Expected 1 argument found 2.')
        return None
    except: 
        pass

    execute.execute_source_code(file_name)


if __name__ == "__main__":
    main()
