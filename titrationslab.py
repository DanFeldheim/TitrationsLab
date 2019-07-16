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
import operator



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
        self.id = Frame(notebook, background = 'alice blue')
        self.naoh = Frame(notebook, background = 'alice blue')
        self.unknown = Frame(notebook, background = 'alice blue')
        self.calcs = Frame(notebook, background = 'alice blue')

        notebook.add(self.id, text = "Student Identifiers")
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
        
        
        # Create entries for student id
        # self.id_Label = ttk.Label(self.id, text = 'Enter Student Identifiers', background = 'blue', foreground = "blue", 
            # relief = RAISED, anchor = CENTER, width = 25,font = self.font1).grid(row = 0, column = 0, padx = 5, pady = (15, 5), sticky = 'e')
        
        self.last = StringVar()
        self.last_label = ttk.Label(self.id, text = 'Last Name:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.last_entry = ttk.Entry(self.id, width = 15, textvariable = self.last)
        self.last_label.grid(row = 0, column = 0, pady = (10, 5))
        self.last_entry.grid(row = 1, column = 0, pady = (1, 5))
        self.last.set('Last Name') 
        
        self.first = StringVar()
        self.first_label = ttk.Label(self.id, text = 'First Name:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.first_entry = ttk.Entry(self.id, width = 15, textvariable = self.first)
        self.first_label.grid(row = 0, column = 1, pady = (10, 5))
        self.first_entry.grid(row = 1, column = 1, pady = (1, 5))
        self.first.set('First Name') 
        
        self.student_id = StringVar()
        self.student_id_label = ttk.Label(self.id, text = 'ID Number', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.student_id_entry = ttk.Entry(self.id, width = 15, textvariable = self.student_id)
        self.student_id_label.grid(row = 2, column = 0, pady = (10, 5), columnspan = 1)
        self.student_id_entry.grid(row = 3, column = 0, pady = (1, 5), columnspan = 1)
        self.student_id.set('Student ID') 
        
        
        # Create labels for standardization of NaOH table
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
        self.mass1 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass1, width = 6)
        self.import_entry.grid(row = 1, column = 1, pady = (15, 5))
        self.mass1.set('3.0')
        
        self.mass2 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass2, width = 6)
        self.import_entry.grid(row = 1, column = 2, pady = (15, 5))
        self.mass2.set('6.0')
        
        self.mass3 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.mass3, width = 6)
        self.import_entry.grid(row = 1, column = 3, pady = (15, 5))
        self.mass3.set('9.0')
        
        self.init_vol1 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.import_entry.grid(row = 2, column = 1, pady = (15, 5))
        self.init_vol1.set('1.0')
        
        self.init_vol2 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol2, width = 6)
        self.import_entry.grid(row = 2, column = 2, pady = (15, 5))
        self.init_vol2.set('1.0')
        
        self.init_vol3 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.import_entry.grid(row = 2, column = 3, pady = (15, 5))
        self.init_vol3.set('1.0')
        
        self.final_vol1 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol1, width = 6)
        self.import_entry.grid(row = 3, column = 1, pady = (15, 5))
        self.final_vol1.set('1.6')
        
        self.final_vol2 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol2, width = 6)
        self.import_entry.grid(row = 3, column = 2, pady = (15, 5))
        self.final_vol2.set('2.5')
        
        self.final_vol3 = DoubleVar()
        self.import_entry = ttk.Entry(self.naoh, textvariable = self.final_vol3, width = 6)
        self.import_entry.grid(row = 3, column = 3, pady = (15, 5))
        self.final_vol3.set('2.2')
        
        # Calculations tab
    
        # Create label for standardization of NaOH calculations
        self.NaOH_Label = ttk.Label(self.calcs, text = 'Standardization of NaOH', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 21, font = self.font1).grid(row = 0, column = 1, columnspan = 1, pady = (15, 5))
        
        self.trial_Label = ttk.Label(self.calcs, text = 'Enter NaOH Molarity \n      for Each Trial', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 20, font = self.font2).grid(row = 1, column = 1, columnspan = 1, pady = (15, 5))
            
        # Create entry boxes for molarities
        self.M1 = DoubleVar()
        self.M1_label = ttk.Label(self.calcs, text = 'Trial 1', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M1_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M1)
        self.M1_label.grid(row = 2, column = 0, pady = (10, 5))
        self.M1_entry.grid(row = 3, column = 0, pady = (1, 5))
        self.M1.set(1)   
        
        self.M2 = DoubleVar()
        self.M2_label = ttk.Label(self.calcs, text = 'Trial 2', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M2_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M2)
        self.M2_label.grid(row = 2, column = 1, pady = (10, 5))
        self.M2_entry.grid(row = 3, column = 1, pady = (1, 5))
        self.M2.set(1)  
            
        self.M3 = DoubleVar()
        self.M3_label = ttk.Label(self.calcs, text = 'Trial 3', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 10, font = self.font2)
        self.M3_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M3)
        self.M3_label.grid(row = 2, column = 2, pady = (10, 5))
        self.M3_entry.grid(row = 3, column = 2, pady = (1, 5))
        self.M3.set(1)      
            
        self.avg = DoubleVar()
        self.avg_label = ttk.Label(self.calcs, text = 'Average Molarity', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.avg_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.avg)
        self.avg_label.grid(row = 4, column = 1, pady = (10, 5))
        self.avg_entry.grid(row = 5, column = 1, pady = (1, 5))
        self.avg.set(1)  
        
        # Create button that calls function for selecting files for analysis
        self.openFileButton = ttk.Button(self.calcs, text = 'Calculate', style = "TButton", command = lambda: self.get_naoh_molarity_values())
        self.openFileButton.grid(row = 6, column = 1, pady = (1, 5))

            
        # Function to calculate molarity of NaOH in the standardization of NaOH experiment
    def get_naoh_molarity_values(self):
        
        try:
            
            # Get data from trial 1-3 entry boxes
            self.mass_khp1 = self.mass1.get()
            self.mass_khp2 = self.mass2.get()
            self.mass_khp3 = self.mass3.get()
                
            self.vi1 = self.init_vol1.get()
            self.vi2 = self.init_vol2.get()
            self.vi3 = self.init_vol3.get()
                
            self.vf1 = self.final_vol1.get()
            self.vf2 = self.final_vol2.get()
            self.vf3 = self.final_vol3.get()
                
            self.average = self.avg.get()
            
            self.molarity1 = self.M1.get()
            self.molarity2 = self.M2.get()
            self.molarity3 = self.M3.get()
            self.avg_molarity = self.avg.get()
            
            self.calc_naoh_molarity()
            
        except ValueError:
            
            messagebox.showinfo('Message', 'Please fill in all entry boxes.')
            
        
    # Calculate average molarity based upon the khp masses and volumes entered in standardization of NaOH tab
    def calc_naoh_molarity(self):
        

        # Create lists for values so calculation can be run in a loop
        self.mass_khp_list = [self.mass_khp1, self.mass_khp2, self.mass_khp3]
        self.vi_list = [self.vi1, self.vi2, self.vi3]
        self.vf_list = [self.vf1, self.vf2, self.vf3]
        
        # Loop through lists to calculate moles of khp and molarity of NaOH
        # Create lists for results
        
        self.moles_khp_list = []
        self.molarity_naoh = []
        
        for mass in self.mass_khp_list:
            self.moles_khp = mass/204.22
            self.moles_khp_list.append(self.moles_khp)
        
        # Calculate average molarity and add to moles list
        self.avg_moles_khp = sum(self.moles_khp_list)/3
        self.moles_khp_list.append(self.avg_moles_khp)
        
        # Round number in list to hundredths place
        self.rounded_moles_khp_list = [round(i, 2) for i in self.moles_khp_list]
        
        print ('Moles khp: ' + str(self.rounded_moles_khp_list))
    
        
        # Calculate NaOH molarity for each trial and then average
        # Calculate Vf - Vi for each element in vi_list and vf_list and add to list
        self.vol_diff_list = map(operator.sub, self.vf_list, self.vi_list)
        
        print('Volume difference = ' + str(self.vol_diff_list))
        
        # Use zip to to grap corresponding elements from vol and moles lists and calculate
        # Create a molarity list for results
        self.naoh_molarity_list = []
        for moles, vol in zip(self.moles_khp_list, self.vol_diff_list):
            self.molarity = 1000*(moles/vol)
            self.naoh_molarity_list.append(self.molarity)    
                    
        # Calculate average and append to list
        self.avg_molarity = sum(self.naoh_molarity_list)/3
        self.naoh_molarity_list.append(self.avg_molarity)
        
        print ('molarity = ' + str(self.naoh_molarity_list))
        
        # print (type(self.naoh_molarity_list[3]))
        
        # Round values to 2 decimal places
        self.rounded_naoh_molarity_list = [round(i, 2) for i in self.naoh_molarity_list]
            
        print('Molarity = ' + str(self.rounded_naoh_molarity_list))
       
       
                
            
        
       
            
            
            
        
#----------------------------------------------------------------------------------------------

# Execute application
# Create main page
root = tk.Tk()
b = titrate(root)
root.mainloop()




















