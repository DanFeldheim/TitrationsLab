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
    
    # Define function that sets up the tkinter GUI
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
        
        # Create labels for Trial table
        # Trial 1 label
        self.data_Label = ttk.Label(self.naoh, text = 'Data', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 10,font = self.font1).grid(row = 0, column = 0, padx = 5, pady = (15, 5))
            
        self.trial_1_Label = ttk.Label(self.naoh, text = 'Trial 1', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 10,font = self.font1).grid(row = 0, column = 1, padx = 5, pady = (15, 5))   
            
        self.trial_2_Label = ttk.Label(self.naoh, text = 'Trial 2', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 10,font = self.font1).grid(row = 0, column = 2, padx = 5, pady = (15, 5))  
            
        self.trial_3_Label = ttk.Label(self.naoh, text = 'Trial 3', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 10,font = self.font1).grid(row = 0, column = 3, padx = 5, pady = (15, 5)) 
            
        self.mass_Label = ttk.Label(self.naoh, text = 'mass KHP (g)', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 12, font = self.font2).grid(row = 1, column = 0, padx = 5, pady = (15, 5)) 
            
        self.mass_Label = ttk.Label(self.naoh, text = 'Vi (mL)', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 12, font = self.font2).grid(row = 2, column = 0, padx = 5, pady = (15, 5)) 
            
        self.mass_Label = ttk.Label(self.naoh, text = 'Vf (mL', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 12, font = self.font2).grid(row = 3, column = 0, padx = 5, pady = (15, 5)) 
            
        # Create entry boxes for data
        # Create entry box to display files selected for analysis
        self.mass1 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass1, width = 6)
        self.import_entry.grid(row = 1, column = 1, pady = (15, 5))
        self.mass1.set('')
        
        self.mass2 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass2, width = 6)
        self.import_entry.grid(row = 1, column = 2, pady = (15, 5))
        self.mass2.set('')
        
        self.mass3 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass3, width = 6)
        self.import_entry.grid(row = 1, column = 3, pady = (15, 5))
        self.mass3.set('')
        
        self.init_vol1 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.import_entry.grid(row = 2, column = 1, pady = (15, 5))
        self.init_vol1.set('')
        
        self.init_vol2 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol2, width = 6)
        self.import_entry.grid(row = 2, column = 2, pady = (15, 5))
        self.init_vol2.set('')
        
        self.init_vol3 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.import_entry.grid(row = 2, column = 3, pady = (15, 5))
        self.init_vol1.set('')
        
        self.final_vol1 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol1, width = 6)
        self.import_entry.grid(row = 3, column = 1, pady = (15, 5))
        self.final_vol1.set('')
        
        self.final_vol2 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol2, width = 6)
        self.import_entry.grid(row = 3, column = 2, pady = (15, 5))
        self.final_vol2.set('')
        
        self.final_vol3 = IntVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol3, width = 6)
        self.import_entry.grid(row = 3, column = 3, pady = (15, 5))
        self.final_vol3.set('')
        
        # Calculations tab
    
        # Create label for standardization of NaOH calculations
        self.NaOH_Label = ttk.Label(self.calcs, text = 'Standardization of NaOH', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 21, font = self.font1).grid(row = 0, column = 1, columnspan = 1, pady = (15, 5))
        
        self.trial_Label = ttk.Label(self.calcs, text = 'Enter NaOH Molarity \n      for Each Trial', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 20, font = self.font2).grid(row = 1, column = 1, columnspan = 1, pady = (15, 5))
            
        # Create entry boxes for molarities
        self.M1 = IntVar()
        self.M1_label = ttk.Label(self.calcs, text = 'Trial 1', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M1_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M1)
        self.M1_label.grid(row = 2, column = 0, pady = (10, 5))
        self.M1_entry.grid(row = 3, column = 0, pady = (1, 5))
        self.M1.set(1)   
        
        self.M2 = IntVar()
        self.M2_label = ttk.Label(self.calcs, text = 'Trial 2', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M2_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M2)
        self.M2_label.grid(row = 2, column = 1, pady = (10, 5))
        self.M2_entry.grid(row = 3, column = 1, pady = (1, 5))
        self.M2.set(1)  
            
        self.M3 = IntVar()
        self.M3_label = ttk.Label(self.calcs, text = 'Trial 3', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M3_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M3)
        self.M3_label.grid(row = 2, column = 2, pady = (10, 5))
        self.M3_entry.grid(row = 3, column = 2, pady = (1, 5))
        self.M3.set(1)      
            
        self.avg = IntVar()
        self.avg_label = ttk.Label(self.calcs, text = 'Average Molarity', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.avg_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.avg)
        self.avg_label.grid(row = 4, column = 1, pady = (10, 5))
        self.avg_entry.grid(row = 5, column = 1, pady = (1, 5))
        self.avg.set(1)  
            
            
            
            
            
            
        
#----------------------------------------------------------------------------------------------

# Execute application
# Create main page
root = tk.Tk()
b = titrate(root)
root.mainloop()




















