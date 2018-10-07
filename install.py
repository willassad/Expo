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

import os
import platform

class InstallExpo():

    def __init__(self):
        print('+------------------------------------------------------+')
        print('|                   Installing Expo                    |')
        print('|               Developed By Will Assad                |')
        print('+------------------------------------------------------+')


    def setup(self):
        # Check the platform and perform install for that platform
        if platform.system() == "Darwin":
            self.mac_osx_install_route()

    def mac_osx_install_route(self):
        # changes the permissions of the fle to make it executable
        os.system("chmod +x ./main.py")
        # Add customised directory to the $PATH
        os.system('export PATH="$PATH:$HOME/bin"')
        # Create a symbolic link to the script
        os.system("ln -s " + os.getcwd() + "/main.py /usr/local/bin/exp")


if __name__ == "__main__":
    installer = InstallExpo()
    installer.setup()
