#!/usr/bin/env python3

''' This program is free software: you can redistribute it and/or modify it under the
	terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
	This program is distributed in the hope that it will be useful, but WITHOUT ANY
    WARRANTY; without even the implied warranty of MERCHANTABILITY or 
    FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with this program. 
    If not, see <https://www.gnu.org/licenses/>.
'''
    
    
    
    
import dearpygui.dearpygui as dpg
import sys
import time
import json



"""
Module Docstring
"""

__author__ = "Sela"
__version__ = "1.0.0"
__license__ = "GPLv3"


def main():
    dpg.create_context()
    dpg.create_viewport(title='Easy Time Manager', width = 500, height = 500)





if __name__ == "__main__":
    main()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
