# Import Packages
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import numpy as np
from numpy import exp, linspace, random
import pandas as pd
import os.path
import glob, os
import os.path
from tkinter import messagebox



class titrate:
    
    def __init__(self, master):
        
        root.title("Lab 3: Titrations")
        root.geometry('650x700+500+300')
        self.COLOR = "alice blue"
        root.config(bg = self.COLOR)

        # Create tabs in root   
        notebook = ttk.Notebook(master, width = 600, height = 600)
        notebook.grid()
        self.naoh = Frame(notebook, background = 'alice blue')
        self.unknown = Frame(notebook, background = 'alice blue')
        self.calcs = Frame(notebook, background = 'alice blue')

        notebook.add(self.naoh, text = "Standardization of NaOH")
        notebook.add(self.unknown, text = "Unknown Acid Titration")
        notebook.add(self.calcs, text = "Calculations")

        # Define fonts 
        # Font for labels
        self.font1 = ('times', 18)
        self.font2 = ('times', 14)

        # Font for buttons
        self.style = ttk.Style(master)
        self.style.configure("TButton", font = ('times', 18), foreground = "red", highlightbackground = 'red')
        
        
#----------------------------------------------------------------------------------------------

# Execute application
# Create main page
root = tk.Tk()
b = titrate(root)
root.mainloop()