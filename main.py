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
    path = os.getcwd() #Holds path this script was executed from

    # Holds the name of the file the user wants to compile
    try: file_name = sys.argv[1]
    except:
        print("ERROR: Expected 1 Argument Containing File Name to be Run e.g 'exp main.expo'")
        return

    # Check if the file extension is correct
    if file_name[len(file_name) - 5:len(file_name)] != ".expo":
        print("ERROR: File extension not recognised please make sure extension is '.expo'")
        return

    #Check to make sure that only one argument is passed
    try:
        print('ERROR: Expected 1 argument found 2 (' + sys.argv[1] + ", " + sys.argv[2] + ')')
        return # quit programme
    except: pass

    execute.execute_source_code(file_name)


if __name__ == "__main__":
    main()
