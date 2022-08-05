#!/usr/bin/env python3


"""
Module Docstring
"""

__author__ = "Sela"
__version__ = "1.0.0"
__license__ = "GPLv3"

#modules
import tkinter
import customtkinter #used for the GUI
import time #used for time tracking (standard lib)
import calendar
import sys #system interactions (standard lib)
import json #saving your personalized settings (standard lib)




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Launcher Window")
        self.geometry("300 x 200")
        self.resizable(width=False, height=False)
        
        self.button = customtkinter.CTkButton(master = self, text = "Set alarm")
        self.button.place(x = 80, y = 10)
        
        self.button = customtkinter.CTkButton(master = self, text = "Set schedule")
        self.button.place(x = 80, y = 50)
        
        self.button = customtkinter.CTkButton(master = self, text = "Create new task")
        self.button.place(x = 80, y = 90)
        
        self.button = customtkinter.CTkButton(master = self, text = "Track task")
        self.button.place(x = 80, y = 130)
        
        self.button = customtkinter.CTkButton(master = self, text = "See calendar")
        self.button.place(x = 80, y = 170)
        




if __name__ == "__main__":
    app = App()
    app.mainloop()

