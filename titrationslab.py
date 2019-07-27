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
import csv



class titrate:
    
    # Define function that sets up the tkinter GUI
    def __init__(self, master):
        
        root.title("Lab 3: Titrations")
        # root.geometry('650x700+500+300')
        root.geometry('700x700+950+600')
        self.COLOR = "alice blue"
        root.config(bg = self.COLOR)

        # Create tabs in root   
        notebook = ttk.Notebook(master, width = 650, height = 650)
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
        
        #---------------------------------------------------------
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
        #-----------------------------------------------------------
        
        
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
        # These were generated as stringvars in order to be able to check that students have
        # entered their numbers to two decimal places. If floats were used then trailing zeros
        # would be lost. For example, 0.30 would always be read by python as 0.3. This
        # would trigger the error message to enter the number to 2 decimal places.
        
        self.mass1 = StringVar()
        self.mass1_entry = ttk.Entry(self.naoh, textvariable = self.mass1, width = 6)
        self.mass1_entry.grid(row = 1, column = 1, pady = (15, 5))
        self.mass1.set('0.3892')
        
        self.mass2 = StringVar()
        self.mass2_entry = ttk.Entry(self.naoh, textvariable = self.mass2, width = 6)
        self.mass2_entry.grid(row = 1, column = 2, pady = (15, 5))
        self.mass2.set('0.3905')
        
        self.mass3 = StringVar()
        self.mass3_entry = ttk.Entry(self.naoh, textvariable = self.mass3, width = 6)
        self.mass3_entry.grid(row = 1, column = 3, pady = (15, 5))
        self.mass3.set('0.3995')
        
        self.init_vol1 = StringVar()
        self.init_vol1_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.init_vol1_entry.grid(row = 2, column = 1, pady = (15, 5))
        self.init_vol1.set('7.00')
        
        self.init_vol2 = StringVar()
        self.init_vol2_entry = ttk.Entry(self.naoh, textvariable = self.init_vol2, width = 6)
        self.init_vol2_entry.grid(row = 2, column = 2, pady = (15, 5))
        self.init_vol2.set('6.20')
        
        self.init_vol3 = StringVar()
        self.init_vol3_entry = ttk.Entry(self.naoh, textvariable = self.init_vol3, width = 6)
        self.init_vol3_entry.grid(row = 2, column = 3, pady = (15, 5))
        self.init_vol3.set('2.60')
        
        self.final_vol1 = StringVar()
        self.final_vol1_entry = ttk.Entry(self.naoh, textvariable = self.final_vol1, width = 6)
        self.final_vol1_entry.grid(row = 3, column = 1, pady = (15, 5))
        self.final_vol1.set('25.87')
        
        self.final_vol2 = StringVar()
        self.final_vol2_entry = ttk.Entry(self.naoh, textvariable = self.final_vol2, width = 6)
        self.final_vol2_entry.grid(row = 3, column = 2, pady = (15, 5))
        self.final_vol2.set('24.30')
        
        self.final_vol3 = StringVar()
        self.final_vol3_entry = ttk.Entry(self.naoh, textvariable = self.final_vol3, width = 6)
        self.final_vol3_entry.grid(row = 3, column = 3, pady = (15, 5))
        self.final_vol3.set('21.99')
        
        
        #--------------------------------------------------------
        # Unknown Acid Titration tab
        
        # Create label for the color endpoint
        self.unknown_Label = ttk.Label(self.unknown, text = 'Quick Trial (Color End Point)', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 30,font = self.font1).grid(row = 0, column = 0, padx = 5, pady = (1, 5))
            
        # Create entry boxes
        self.vol_acid = StringVar()
        self.vol_acid_label = ttk.Label(self.unknown, text = 'Enter volume of acid titrated (mL)', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 30, font = self.font2)
        self.vol_acid_label.grid(row = 1, column = 0, pady = (1, 5))
        self.vol_acid_entry = ttk.Entry(self.unknown, textvariable = self.vol_acid, width = 6)
        self.vol_acid_entry.grid(row = 2, column = 0, pady = (1, 5))
        self.vol_acid.set('25.00')
        
        # Create pull down menu for unknown acid
        self.unk = StringVar()
        self.unk_label = ttk.Label(self.unknown, text = 'Unknown Acid:', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.unk_label.grid(row = 3, column = 0, pady = (1, 5), padx = 3)
        self.unk_box = ttk.Combobox(self.unknown, textvariable = self.unk, width = 12, font = self.font2)
        self.unk_box.config(values = ('A', 'B', 'C', 'D', 'E', 'F'))
        self.unk_box.grid(row = 4, column = 0, pady = (1, 5), padx = 3)

        self.init_buret = StringVar()
        self.init_buret_label = ttk.Label(self.unknown, text = 'Enter initial buret reading (mL)', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 30, font = self.font2)
        self.init_buret_label.grid(row = 5, column = 0, pady = (1, 5))
        self.init_buret_entry = ttk.Entry(self.unknown, textvariable = self.init_buret, width = 6)
        self.init_buret_entry.grid(row = 6, column = 0, pady = (1, 5))
        self.init_buret.set('5.65')
        
        self.final_buret = StringVar()
        self.final_buret_label = ttk.Label(self.unknown, text = 'Enter final buret reading at color change (mL)', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 38, font = self.font2)
        self.final_buret_label.grid(row = 7, column = 0, pady = (1, 5))
        self.final_buret_entry = ttk.Entry(self.unknown, textvariable = self.final_buret, width = 6)
        self.final_buret_entry.grid(row = 8, column = 0, pady = (1, 5))
        self.final_buret.set('34.82')
        
        # Create label for the pH endpoint
        self.pH_Label = ttk.Label(self.unknown, text = 'pH Titration', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 15,font = self.font1).grid(row = 9, column = 0, padx = 5, pady = (15, 5))
            
        # Create label for the pH endpoint
        self.pH2_Label = ttk.Label(self.unknown, text = 'Enter the pH at the 1/4 Veq, 1/2 Veq, and 3/4 Veq', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 40,font = self.font2).grid(row = 10, column = 0, padx = 5, pady = (5, 5))
            
        self.quarter_pH = StringVar()
        self.quarter_pH_label = ttk.Label(self.unknown, text = 'pH at 1/4 Veq:', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 15, font = self.font2)
        self.quarter_pH_label.grid(row = 11, column = 0, pady = (5, 5))
        self.quarter_pH_entry = ttk.Entry(self.unknown, textvariable = self.quarter_pH, width = 6)
        self.quarter_pH_entry.grid(row = 12, column = 0, pady = (5, 5))
        self.quarter_pH.set('3.15')   
        
        self.half_pH = StringVar()
        self.half_pH_label = ttk.Label(self.unknown, text = 'pH at 1/2 Veq:', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 15, font = self.font2)
        self.half_pH_label.grid(row = 13, column = 0, pady = (5, 5))
        self.half_pH_entry = ttk.Entry(self.unknown, textvariable = self.half_pH, width = 6)
        self.half_pH_entry.grid(row = 14, column = 0, pady = (5, 5))
        self.half_pH.set('3.60')
        
        self.three_quarter_pH = StringVar()
        self.three_quarter_pH_label = ttk.Label(self.unknown, text = 'pH at 3/4 Veq:', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 15, font = self.font2)
        self.three_quarter_pH_label.grid(row = 15, column = 0, pady = (5, 5))
        self.three_quarter_pH_entry = ttk.Entry(self.unknown, textvariable = self.three_quarter_pH, width = 6)
        self.three_quarter_pH_entry.grid(row = 16, column = 0, pady = (5, 5))
        self.three_quarter_pH.set('4.05')
        
        self.mL_naoh_to_equiv = StringVar()
        self.mL_naoh_to_equiv_label = ttk.Label(self.unknown, text = 'mL NaOH to equivalence point:', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 25, font = self.font2)
        self.mL_naoh_to_equiv_label.grid(row = 17, column = 0, pady = (5, 5))
        self.mL_naoh_to_equiv_entry = ttk.Entry(self.unknown, textvariable = self.mL_naoh_to_equiv, width = 6)
        self.mL_naoh_to_equiv_entry.grid(row = 18, column = 0, pady = (5, 5))
        self.mL_naoh_to_equiv.set('27.20')
        
        
        
        
        #--------------------------------------------------------
        # Calculations tab
    
        # Setup widgets
        
        # Widgets for NaOH standardization 
        # Create label for standardization of NaOH calculations
        self.NaOH_Label = ttk.Label(self.calcs, text = 'Standardization of NaOH', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 21, font = self.font1).grid(row = 0, column = 1, columnspan = 1, pady = (15, 5))
        
        self.trial_Label = ttk.Label(self.calcs, text = 'Enter moles KHP and NaOH Molarity for Each Trial', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 45, font = self.font2).grid(row = 1, column = 1, columnspan = 1, pady = (1, 5))
            
        # Create entry boxes for moles khp 
        self.M1 = StringVar()
        self.M1_label = ttk.Label(self.calcs, text = 'Trial 1', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 13, font = self.font2)
        self.M1_label2 = ttk.Label(self.calcs, text = 'KHP:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 4, font = self.font2)
        self.M1_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.M1)
        self.M1_label.grid(row = 2, column = 0, pady = (10, 5), sticky = 'e')
        self.M1_label2.grid(row = 3, column = 0, pady = (1, 5), sticky = 'w')
        self.M1_entry.grid(row = 3, column = 0, pady = (1, 5), sticky = 'e')
        self.M1.set('0.001910')   
        
        self.M2 = StringVar()
        self.M2_label = ttk.Label(self.calcs, text = 'Trial 2', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.M2_entry = ttk.Entry(self.calcs, width = 8, textvariable = self.M2)
        self.M2_label.grid(row = 2, column = 1, pady = (10, 5))
        self.M2_entry.grid(row = 3, column = 1, pady = (1, 5))
        self.M2.set('0.001910')  
            
        self.M3 = StringVar()
        self.M3_label = ttk.Label(self.calcs, text = 'Trial 3', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.M3_entry = ttk.Entry(self.calcs, width = 8, textvariable = self.M3)
        self.M3_label.grid(row = 2, column = 2, pady = (10, 5))
        self.M3_entry.grid(row = 3, column = 2, pady = (1, 5))
        self.M3.set('0.001910')      
        
        # Create entry boxes for NaOH molarities
        self.Na1 = StringVar()
        self.Na1_label = ttk.Label(self.calcs, text = 'NaOH:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 6, font = self.font2)
        self.Na1_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.Na1)
        self.Na1_label.grid(row = 4, column = 0, pady = (1, 5), sticky = 'w')
        self.Na1_entry.grid(row = 4, column = 0, pady = (1, 5), sticky = 'e')
        self.Na1.set('0.1010')   
        
        self.Na2 = StringVar()
        self.Na2_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.Na2)
        self.Na2_entry.grid(row = 4, column = 1, pady = (1, 5))
        self.Na2.set('0.1056')  
            
        self.Na3 = StringVar()
        self.Na3_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.Na3)
        self.Na3_entry.grid(row = 4, column = 2, pady = (1, 5))
        self.Na3.set('0.1009')       
        
        self.naavg = StringVar()
        self.naavg_label1 = ttk.Label(self.calcs, text = 'Average NaOH Molarity:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 20, font = self.font2)
        self.naavg_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.naavg)
        self.naavg_label1.grid(row = 5, column = 0, columnspan = 2, pady = (15, 5), padx = 20)
        self.naavg_entry.grid(row = 5, column = 1, columnspan = 2, pady = (15, 5))
        self.naavg.set('0.1009')  
        
        # Widgets for unknown titration
        self.unknown_label = ttk.Label(self.calcs, text = 'Titration of an Unknown Weak Acid', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 35, font = self.font1).grid(row = 10, column = 1, columnspan = 1, pady = (25, 5))
            
        self.color_molarity = StringVar()
        self.color_molarity_label = ttk.Label(self.calcs, text = 'Enter the acid molarity (M) based upon the color endpoint:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 50, font = self.font2)
        self.color_molarity_entry = ttk.Entry(self.calcs, width = 10, textvariable = self.color_molarity)
        self.color_molarity_label.grid(row = 11, column = 1, pady = (1, 5))
        self.color_molarity_entry.grid(row = 12, column = 1, pady = (1, 10))
        self.color_molarity.set('0.1178')  
        
        self.accurate_molarity = StringVar()
        self.accurate_molarity_label = ttk.Label(self.calcs, text = 'Enter the acid molarity (M) based upon accurate pH titration:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 50, font = self.font2)
        self.accurate_molarity_entry = ttk.Entry(self.calcs, width = 10, textvariable = self.accurate_molarity)
        self.accurate_molarity_label.grid(row = 13, column = 1, pady = (1, 5))
        self.accurate_molarity_entry.grid(row = 14, column = 1, pady = (1, 20))
        self.accurate_molarity.set('0.1098')  
        
        self.quarter_equiv = StringVar()
        self.quarter_equiv_label = ttk.Label(self.calcs, text = 'Enter pKa from 1/4 Veq:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 20, font = self.font2)
        self.quarter_equiv_entry = ttk.Entry(self.calcs, width = 5, textvariable = self.quarter_equiv)
        self.quarter_equiv_label.grid(row = 15, column = 0, columnspan = 2, pady = (1, 5))
        self.quarter_equiv_entry.grid(row = 15, column = 1, columnspan = 2, pady = (1, 5))
        self.quarter_equiv.set('3.63')  
        
        self.half_equiv = StringVar()
        self.half_equiv_label = ttk.Label(self.calcs, text = 'Enter pKa from 1/2 Veq:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 20, font = self.font2)
        self.half_equiv_entry = ttk.Entry(self.calcs, width = 5, textvariable = self.half_equiv)
        self.half_equiv_label.grid(row = 16, column = 0, columnspan = 2, pady = (1, 5))
        self.half_equiv_entry.grid(row = 16, column = 1, columnspan = 2, pady = (1, 5))
        self.half_equiv.set('3.60')  
        
        self.three_quarter_equiv = StringVar()
        self.three_quarter_equiv_label = ttk.Label(self.calcs, text = 'Enter pKa from 1/2 Veq:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 20, font = self.font2)
        self.three_quarter_equiv_entry = ttk.Entry(self.calcs, width = 5, textvariable = self.three_quarter_equiv)
        self.three_quarter_equiv_label.grid(row = 17, column = 0, columnspan = 2, pady = (1, 5))
        self.three_quarter_equiv_entry.grid(row = 17, column = 1, columnspan = 2, pady = (1, 5))
        self.three_quarter_equiv.set('3.57')  
        
        self.avg_pka = StringVar()
        self.avg_pka_label = ttk.Label(self.calcs, text = 'Enter average pKa:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 20, font = self.font2)
        self.avg_pka_entry = ttk.Entry(self.calcs, width = 5, textvariable = self.avg_pka)
        self.avg_pka_label.grid(row = 18, column = 0, columnspan = 2, pady = (1, 5))
        self.avg_pka_entry.grid(row = 18, column = 1, columnspan = 2, pady = (1, 5))
        self.avg_pka.set('3.60') 
        
        # Create pull down menu for student's choice for the unknown acid
        self.student_guess = StringVar()
        self.student_guess_label = ttk.Label(self.calcs, text = 'Unknown Acid:', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 18, font = self.font2)
        self.student_guess_label.grid(row = 19, column = 0, columnspan = 2, pady = (1, 5), padx = 3)
        self.student_guess_box = ttk.Combobox(self.calcs, textvariable = self.student_guess, width = 8, font = self.font2)
        self.student_guess_box.config(values = ('Acetic Acid', 'Formic Acid', 'HI', 'HBr', 'Carbonic', 'Propionic'))
        self.student_guess_box.grid(row = 19, column = 1, columnspan = 2, pady = (1, 5), padx = 3)
        
        
        # Create button that runs program
        self.openFileButton = ttk.Button(self.calcs, text = 'Submit for Grading', style = "TButton", command = lambda: self.get_values())
        self.openFileButton.grid(row = 20, column = 1, pady = (25, 5))
         
        # Start a counter for the number of times the submit button is presses
        self.submit_counter = 0    
    
# Function to retrieve all values entered by student and check that they were entered to the correct number of sig figs

    def get_values(self):
        
        # Increase counter
        self.submit_counter += 1
        
        # From unknown tab
        self.acid = self.vol_acid.get()
        self.buret1 = self.init_buret.get()
        self.buret2 = self.final_buret.get()
        self.quarter_Veq_pH = self.quarter_pH.get()
        self.half_Veq_pH = self.half_pH.get()
        self.threeQuart_Veq_pH = self.three_quarter_pH.get()
            
        # From NaOH tab
        self.mass_khp1 = self.mass1.get()
        self.mass_khp2 = self.mass2.get()
        self.mass_khp3 = self.mass3.get()
                
        self.vi1 = self.init_vol1.get()
        self.vi2 = self.init_vol2.get()
        self.vi3 = self.init_vol3.get()
                
        self.vf1 = self.final_vol1.get()
        self.vf2 = self.final_vol2.get()
        self.vf3 = self.final_vol3.get()
                
        # From calculations tab
        self.khp_moles1 = self.M1.get()
        self.khp_moles2 = self.M2.get()
        self.khp_moles3 = self.M3.get()
        
        self.naoh_molarity1 = self.Na1.get()
        self.naoh_molarity2 = self.Na2.get()
        self.naoh_molarity3 = self.Na3.get()
        self.naoh_avg = self.naavg.get()
        
        self.color_titration = self.color_molarity.get()
        self.accurate_titration = self.accurate_molarity.get()
        self.quarter_pt = self.quarter_equiv.get()
        self.half_pt = self.half_equiv.get()
        self.three_pt = self.three_quarter_equiv.get()
        self.average_pka = self.avg_pka.get()
        
        
        # Check that all values are entered and are out to the correct number of decimal places
        # Place all values that go out two decimals places in a list 
        self.two_decimals_list = [self.acid, self.buret1, self.buret2, self.quarter_Veq_pH, self.half_Veq_pH, 
            self.threeQuart_Veq_pH, self.vi1, self.vi2, self.vi3, self.vf1, self.vf2, self.vf3, self.quarter_pt, 
            self.half_pt, self.three_pt, self.average_pka]
            
        # Place all values that go out four decimals places in a list 
        self.four_decimals_list = [self.mass_khp1, self.mass_khp2, self.mass_khp3, self.naoh_molarity1, self.naoh_molarity2, 
        self.naoh_molarity3, self.naoh_avg, self.color_titration, self.accurate_titration]
            
        # Place all values that go out six decimals places in a list 
        self.six_decimals_list = [self.khp_moles1, self.khp_moles2, self.khp_moles3]    
            
        # If NA in list, delete it
        while 'NA' in self.two_decimals_list: self.two_decimals_list.remove('NA') 
        while 'NA' in self.four_decimals_list: self.four_decimals_list.remove('NA')
        while 'NA' in self.six_decimals_list: self.six_decimals_list.remove('NA')
        
        # Loop through each list, split the string around the decimal pt, and check for length
        # Start a list for yes/no depending on whether each value was entered correctly
        self.correct_list1 = []
        for val in self.two_decimals_list:
            y = val.split('.')
            if len(y[-1]) != 2:
                self.correct_list1.append('no')
                    
            else:
                self.correct_list1.append('yes')
                
        self.correct_list2 = []
        for entry in self.four_decimals_list:
            y = entry.split('.')
            if len(y[-1]) != 4:
                self.correct_list2.append('no')
                    
            else:
                self.correct_list2.append('yes')
          
        self.correct_list3 = []
        for entry in self.six_decimals_list:
            y = entry.split('.')
            if len(y[-1]) != 6:
                self.correct_list3.append('no')
                    
            else:
                self.correct_list3.append('yes')      
                    
        # If either list contains a no, go to error message
        if 'no' in self.correct_list1 or 'no' in self.correct_list2 or 'no' in self.correct_list3:
            self.decimal_error()
            
        else:
            self.calc_moles_khp()
            
 
# Functions to calculate correct answers based upon raw data entered by students
   
    # Moles khp based upon masses entered by students
    
    # Calculate average moles based upon the khp masses entered in standardization of NaOH tab
    # Strategy for dealing with NA: Convert NA to float -999.99 and perform moles calculation. Then delete
    # negative moles, and calculate average moles with remaining numbers.
    
    def calc_moles_khp(self):

        # Create list for trials 1-3 of mass khp  
        
        self.mass_khp_list = [self.mass_khp1, self.mass_khp2, self.mass_khp3]
        
        # Create list for results
        self.correct_moles_khp_list = []
        
        for mass in self.mass_khp_list:
            if mass == 'NA':
                self.correct_moles_khp_list.append('NA')
                print('mass khp = ' + mass)
                print('')
                
            else:    
                # Convert mass to float
                mass = float(mass)
          
                # Calculate moles and append result to list
                self.moles_khp = mass/204.22
                self.correct_moles_khp_list.append(self.moles_khp)
        
        print ('Moles khp before rounding: ' + str(self.correct_moles_khp_list))
        print('')
        
        
        self.calc_naoh_molarity()
        
        
    # Function to calculate NaOH molarity
    
    # Use same strategy as above for dealing with NA
    # The strategy is particularly important here as elements in each list must be kept aligned.
    # That is, vf1 must be subtracted from vi1. Simply removing NAs rather than replacing with a 
    # float like 999.99 could make one list shorther than the other and cause misalignment.
    
    def calc_naoh_molarity(self):
        
        # Build trial volume lists
        self.vi_list = [self.vi1, self.vi2, self.vi3]
        self.vf_list = [self.vf1, self.vf2, self.vf3]
        
        # Calculate NaOH molarity for each trial and then average
        # Calculate Vf - Vi for each element in vi_list and vf_list and add to list
        
        # Create a volume difference list
        self.vol_diff_list = []
        
        for initial_vol, final_vol in zip(self.vi_list, self.vf_list):
            if initial_vol == 'NA' or final_vol == 'NA':
                self.vol_diff_list.append('NA')
                
            else:
                # Convert to float
                initial_vol = float(initial_vol)
                final_vol = float(final_vol)
                # Take difference
                self.vol_diff = final_vol - initial_vol
                self.vol_diff_list.append(self.vol_diff)
                
        
        print('Volume Difference = ' + str(self.vol_diff_list))
        print('')
        
        # Use zip to grab corresponding elements from vol and moles lists and calculate NaOH molarity for each trial
        # Create a molarity list for results
        self.naoh_molarity_list = []
        
        for moles, vol in zip(self.correct_moles_khp_list, self.vol_diff_list):
            
            # If an element in either list contains NA, move on.
            if moles == 'NA' or vol == 'NA':
                
                self.naoh_molarity_list.append('NA')
                
            else:
            
                self.molarity = 1000*(moles/vol)
                self.naoh_molarity_list.append(self.molarity)    
                    
        # Calculate average and append to list
        # Need to remove NA from list first
        self.avg_naoh_list = self.naoh_molarity_list
        while 'NA' in self.avg_naoh_list: self.avg_naoh_list.remove('NA')
        self.avg_naoh_molarity = sum(self.avg_naoh_list)/len(self.avg_naoh_list)
        
        # Append the average to the original list self.naoh_molarity_list
        self.naoh_molarity_list.append(self.avg_naoh_molarity)
        
        # Round values to 6 decimal places
        # self.rounded_naoh_molarity_list = [round(i, 6) for i in self.naoh_molarity_list]
            
        print('NaOH Molarity = ' + str(self.naoh_molarity_list))
        print('')
        
        
        # Call acid_molarity_calc for unknown acid titration calculations
        self.acid_molarity_calc()
        
        
    # Calculations for unknown acid titration
    
    # Acid molarity
    def acid_molarity_calc(self):
        
        # Formula: mols acid/vol of acid titrated where volume of acid titrated = self.acid
        # and mols acid = self.buret2 - self.buret1 * self.avg_naoh_molarity * 0.001
        # To base this on the student's naoh molarity use float(self.naavg.get() in place of self.avg_naoh_molarity
        
        # Make sure a numbers were entered for self.buret 1 and 2, and self.naavg
        try:
            self.buret1 and self.buret2 and self.naavg
            self.acid_mols = (float(self.buret2) - float(self.buret1) * float(self.naavg.get()) * 0.001)
            print ('acid mols = ' + str(self.acid_mols))
            print ('')
            
            self.acid_molarity = float(self.acid_mols)/float(self.acid)
            print('acid Molarity = ' + str(self.acid_molarity))   
            print('')
        
            # Call grading functions
            self.pka_calcs()
            
        except ValueError:
            print ('NA entered for self.naavg')
            self.no_average_entered()
            self.naoh_score()
        
        
    # pKa calculations
    # Formula: pKa = pH - log [B]/[A]
    # pH = self.quarter_Veq_pH, self.half_Veq_pH, and self.threeQuart_Veq_pH 
    def pka_calcs(self):
        
        # Create a list for pK values so that average pKa can be calculated based upon the 
        # number of pKa values provided by student. 
        
        self.pKa_list = []
        
        if self.quarter_Veq_pH != 'NA':
            self.pK1 = float(self.quarter_Veq_pH) + 0.477
            self.pKa_list.append(self.pK1)
            
        else:
            self.pK1 = 'NA'
            self.pKa_list.append(self.pK1)
            print('pKa 1/4 Veq not entered.')
            print('')
            
        if self.half_Veq_pH != 'NA':
            self.pK2 = float(self.half_Veq_pH)
            self.pKa_list.append(self.pK2)
        
        else:
            self.pK2 = 'NA'
            self.pKa_list.append(self.pK2)
            print('pKa 1/2 Veq not entered.')
            print('')
                  
        if self.threeQuart_Veq_pH != 'NA':
            self.pK3 = float(self.threeQuart_Veq_pH) - 0.477
            self.pKa_list.append(self.pK3)
            
        else:
            self.pK3 = 'NA'
            self.pKa_list.append(self.pK3)
            print('pKa 3/4 Veq not entered.')
            print('')
        
        print ('pK 1/4 Veq = ' + str(self.pK1))
        print ('')
        print ('pK 1/2 Veq = ' + str(self.pK2))
        print ('')
        print ('pK 3/4 Veq = ' + str(self.pK3))
        print ('') 
        
        # Remove NA so average pKa can be calculated
        # Make a copy
        self.pKa_list_noNA = self.pKa_list
        while 'NA' in self.pKa_list_noNA: self.pKa_list_noNA.remove('NA') 
        
        # Calculate average 
        self.pKa_avg = sum(self.pKa_list_noNA)/len(self.pKa_list_noNA)
        
        
        self.pKa_score()
        
# Scoring functions

    # Function to calculate points for student pKa values
    
    def pKa_score(self):
        # Build a list of pKa values entered by student
        self.student_pKa_list = [self.quarter_pt, self.half_pt, self.three_pt, self.average_pka]
        
        # Create a list of correct pKa values including NA values
        self.correct_pKa_list = [self.pK1, self.pK2, self.pK3, self.pKa_avg]
        
        # Award 2 points for a each correct response
        # Pop up message if incorrect so they can try again
            
        # Start counter for khp points
        self.pK_pts = 0
        
        # Create list for correct vs incorrect pKa responses
        self.number_correct_pK = []
        
        for student_pK, correct_pK in zip(self.student_pKa_list, self.correct_pKa_list):
            
            print('correct pKa list: ' + str(self.correct_pKa_list))
            print('')
            print('student pKa list: ' + str(self.student_pKa_list))
            print('')
            
            
            # If self.student_pK_replaced has -999.99 it in, move on
            if student_pK == 'NA' or correct_pK == 'NA':
                
                print('Oops, this pKa answer was not submitted!')
                
                
            else:
                # Convert student_pK to float
                student_pK = float(student_pK)
                
                # Convert correct_pK to float
                correct_pK = float(correct_pK)
            
                # Set upper and lower limits for correct answer
                self.upper_pK = round(correct_pK + 0.02 * correct_pK, 2)
                self.lower_pK = round(correct_pK - 0.02 * correct_pK, 2)
                
                print('upper correct pK: ' + str(self.upper_pK))
                print('')
                print('lower correct_pK: ' + str(self.lower_pK))
                print('')
                
                if self.upper_pK >= student_pK >= self.lower_pK:
                    self.pK_pts += 2
                    self.number_correct_pK.append('correct')
                        
                else:
                    self.number_correct_pK.append('incorrect')
                    
       
        if 'incorrect' in self.number_correct_pK:
            
            self.check_pK_answer()
            
        
        self.naoh_score()
        

    # Define a function that assigns points based upon correct calculation of moles khp and 
    # NaOH molarity entered
    # A correct response is one that is within 2% of the correct answer 
    # This could be expanded to grade other entries
    
    def naoh_score(self):
            
        # Build list of moles khp entered by student
        self.student_moles_khp_list = [self.khp_moles1, self.khp_moles2, self.khp_moles3]
        print ('Student moles khp list: ' + str(self.student_moles_khp_list))
        print('')
            
        
        # Award 2 points for a each correct response
        # Pop up message if incorrect so they can try again
            
        # Start counter for khp points
        self.khp_pts = 0
        
        # Create list to track correct vs incorrect responses
        self.number_correct_khp = []
           
        for student_moles_khp, correct_moles_khp in zip(self.student_moles_khp_list, self.correct_moles_khp_list):
            
            if student_moles_khp == 'NA' or correct_moles_khp == 'NA':
                print('Oops, this answer was not submitted!')
                
            else:
                
                # Convert student_moles_khp and correct_moles_khp to float
                student_moles_khp = float(student_moles_khp)
                correct_moles_khp = float(correct_moles_khp)
                
                # Set upper and lower limits for correct answer
                self.upper_khp = correct_moles_khp + 0.02 * correct_moles_khp
                self.lower_khp = correct_moles_khp - 0.02 * correct_moles_khp
                
                print('upper correct_moles khp: ' + str(self.upper_khp))
                print('')
                print('lower correct_moles khp: ' + str(self.lower_khp))
                print('')
                
                if self.upper_khp >= student_moles_khp >= self.lower_khp:
                    self.khp_pts += 2
                    # Append correct to list
                    self.number_correct_khp.append('correct')
                        
                else:
                    # Append incorrect to list
                    self.number_correct_khp.append('incorrect')
                    
                    
        # Check list for incorrect response and if present call popup
        if 'incorrect' in self.number_correct_khp:
            self.check_khp_answer()
                    
        
    # Repeat for naoh
    
        # Start counter for NaOH points
        self.naoh_points = 0
        
        try:
            
            self.student_naoh = float(self.naavg.get())
            
            # Calculate 2% above and below the calculated average naoh molarity
            self.lower_naoh = self.avg_naoh_molarity - 0.02 * self.avg_naoh_molarity
            self.upper_naoh = self.avg_naoh_molarity + 0.02 * self.avg_naoh_molarity
            
            # Award 6 points for a correct response, 1 point for incorrect response
            if self.lower_naoh < self.student_naoh < self.upper_naoh:
                self.naoh_points = 6
                     
        except ValueError:
            
            print('NA entered for average NaOH molarity')
            
        self.acid_prediction()
        
        
    # Function to check if they picked the right acid
    def acid_prediction(self):
        
     # Get unkown from drop-down menu (A-F) and assign an acid   
            
        if self.unk.get() == 'A':
            
            self.unk_acid = 'Acetic Acid'
                
        elif self.unk.get() == 'B':
                
            self.unk_acid = 'Formic Acid'
                    
        elif self.unk.get() == 'C':
                
            self.unk_acid = 'HI'
                
        elif self.unk.get() == 'D':
                
            self.unk_acid = 'HBr'
                
        elif self.unk.get() == 'E':
                
            self.unk_acid = 'Carbonic'
                
        elif self.unk.get() == 'F':
                
            self.unk_acid = 'Propionic'
            
        else:
            
            self.no_unk_selected()
            
        print('unk acid: ' + self.unk_acid)
                
        # Get student's answer
        # Start counter for points
        self.unk_pts = 0
            
        # Get student's unknown guess
        self.guess = self.student_guess.get()
            
        # Compare with correct unknown and give points for correct answer
        if self.guess == '':
            self.no_acid_guess_selected()
        
        elif self.guess == self.unk_acid:
            self.unk_pts += 5
                
        else:
            # Call message that the wrong acid was chosen
            self.wrong_acid()
                    
            
        self.calculate_pts()          
  
# Function to add up all of the points
          
    def calculate_pts(self):
        
        print ('khp points = ' + str(self.khp_pts))
        print('')
        
        print ('NaOH points = ' + str(self.naoh_points))
        print('')
        
        print ('pKa points = ' + str(self.pK_pts))
        print('')
        
        print ('Determination of unknown = ' + str(self.unk_pts))
        print('')
            
        # Calculate total points
        self.total_pts = self.khp_pts + self.naoh_points + self.pK_pts + self.unk_pts
            
        # Popup message for the number of points earned
        messagebox.showinfo('Message', 'You earned ' + str(self.total_pts) + ' out of 25 points on the Titrations Lab!')
            
        # Call function to check number of times student has pressed submit button
        self.check_submits()    
            
    def check_submits(self):
        if self.submit_counter == 3:
            
            # Lay a button to nowhere over the submit button
            self.openFileButton = ttk.Button(self.calcs, text = 'Sorry, you have used all of your submissions.', style = "TButton")
            self.openFileButton.grid(row = 20, column = 1, pady = (25, 5))
            
        # self.create_report()
    
 
# Function to generate final report
    def create_report(self):
        
        # Get student info
        self.last_name = self.last.get()
        self.first_name = self.first.get()
        self.id = self.student_id.get()
        
        # Input pts possible
        self.pts_possible = '25'
        
        # Build list with all info to be exported
        self.report_list = [self.last_name, self.first_name, str(self.id), str(self.khp_pts), str(self.naoh_points), str(self.pK_pts), str(self.unk_pts), str(self.total_pts),
                                    self.pts_possible]
                                    
        # Write to csv file
        # Enter file path
        self.path = '/Users/danfeldheim/Documents/'
        self.file_name = self.last_name + '_' + self.first_name
        
        # Join path and file_name
        self.path_and_file = os.path.join(self.path, self.file_name + '.csv')
        
        # Create list of column headers
        self.headers = ['Last Name', 'First Name', 'id', 'KHP Points', 'NaOH Points', 'pKa Points', 'Unknown Determination', 'Total Points', 'Points Possible']
        
        # Write to csv. Use wb for python 2, w for python 3
        with open(self.path_and_file, 'wb') as myfile: 
            wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
            wr.writerow(self.headers) 
            wr.writerow(self.report_list)
       
                    
                               
#------------------------------------------------------------------------------------------------   
# Define error messages
       
    def decimal_error(self):
        
        messagebox.showinfo('Message', 'Please fill in all entry boxes. Note that volume, pH, and pKa values should go out to two decimal places, mass and molarity values four decimal places, and KHP mole values six decimal places. If you do not have a number to enter, type NA.')
                        
    def no_average_entered(self):
                
        messagebox.showinfo('Message', 'Did you mean to enter NA for your buret reading or average NaOH molarity? Your pH titration data cannot be graded without it!')
            
    def check_khp_answer(self):        
            
        messagebox.showinfo('Message', 'One or more of your answers for moles of KHP are >2% outside of the correct answer. Please try again.')
        
    def check_naoh_answer(self):
        
        messagebox.showinfo('Message', 'Your average NaOH molarity is >2% outside of the correct answer. Please try again.')
        
    def check_pK_answer(self):
        
        messagebox.showinfo('Message', 'One or more of your answers for pKa are >2% outside of the correct answer. Please try again.')
        
    def no_unk_selected(self):
        
        messagebox.showinfo('Message', 'Please choose an unknown acid (A-F) from the drop-down menu.')
        
    def wrong_acid(self):
        
        messagebox.showinfo('Message', 'You chose the wrong acid. Please consider your pKa carefully and select again.')
        
    def no_acid_guess_selected(self):
        
        messagebox.showinfo('Message', 'Would you care to guess what your unknown acid is?')
        
        
#----------------------------------------------------------------------------------------------

# Execute application
# Create main page
root = tk.Tk()
b = titrate(root)
root.mainloop()




















