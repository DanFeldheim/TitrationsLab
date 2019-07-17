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
        self.mass1.set('3.02')
        
        self.mass2 = StringVar()
        self.mass2_entry = ttk.Entry(self.naoh, textvariable = self.mass2, width = 6)
        self.mass2_entry.grid(row = 1, column = 2, pady = (15, 5))
        self.mass2.set('6.05')
        
        self.mass3 = StringVar()
        self.mass3_entry = ttk.Entry(self.naoh, textvariable = self.mass3, width = 6)
        self.mass3_entry.grid(row = 1, column = 3, pady = (15, 5))
        self.mass3.set('9.16')
        
        self.init_vol1 = StringVar()
        self.init_vol1_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.init_vol1_entry.grid(row = 2, column = 1, pady = (15, 5))
        self.init_vol1.set('1.11')
        
        self.init_vol2 = StringVar()
        self.init_vol2_entry = ttk.Entry(self.naoh, textvariable = self.init_vol2, width = 6)
        self.init_vol2_entry.grid(row = 2, column = 2, pady = (15, 5))
        self.init_vol2.set('1.22')
        
        self.init_vol3 = StringVar()
        self.init_vol3_entry = ttk.Entry(self.naoh, textvariable = self.init_vol1, width = 6)
        self.init_vol3_entry.grid(row = 2, column = 3, pady = (15, 5))
        self.init_vol3.set('1.53')
        
        self.final_vol1 = StringVar()
        self.final_vol1_entry = ttk.Entry(self.naoh, textvariable = self.final_vol1, width = 6)
        self.final_vol1_entry.grid(row = 3, column = 1, pady = (15, 5))
        self.final_vol1.set('1.63')
        
        self.final_vol2 = StringVar()
        self.final_vol2_entry = ttk.Entry(self.naoh, textvariable = self.final_vol2, width = 6)
        self.final_vol2_entry.grid(row = 3, column = 2, pady = (15, 5))
        self.final_vol2.set('2.57')
        
        self.final_vol3 = StringVar()
        self.final_vol3_entry = ttk.Entry(self.naoh, textvariable = self.final_vol3, width = 6)
        self.final_vol3_entry.grid(row = 3, column = 3, pady = (15, 5))
        self.final_vol3.set('2.2')
        #--------------------------------------------------------
        # Unknown Acid Titration tab
        
        # Create label for the Unknown Acid Titration tab
        self.unknown_Label = ttk.Label(self.unknown, text = 'Quick Trial (Color End Point)', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 30,font = self.font1).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = (1, 5))
            
        # Create entry boxes
        self.vol_acid = StringVar()
        self.vol_acid_label = ttk.Label(self.unknown, text = 'Enter volume of acid titrated (mL)', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 30, font = self.font2)
        self.vol_acid_label.grid(row = 1, column = 0, pady = (1, 5))
        self.vol_acid_entry = ttk.Entry(self.unknown, textvariable = self.vol_acid, width = 6)
        self.vol_acid_entry.grid(row = 2, column = 0, pady = (1, 5))
        self.vol_acid.set('33.02')
        
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
        self.init_buret.set('50.00')
        
        self.final_buret = StringVar()
        self.final_buret_label = ttk.Label(self.unknown, text = 'Enter final buret reading at color change (mL)', background = 'blue', foreground = "blue", relief = RAISED, 
            anchor = CENTER, width = 38, font = self.font2)
        self.final_buret_label.grid(row = 7, column = 0, pady = (1, 5))
        self.final_buret_entry = ttk.Entry(self.unknown, textvariable = self.final_buret, width = 6)
        self.final_buret_entry.grid(row = 8, column = 0, pady = (1, 5))
        self.final_buret.set('20.00')
        
            
        
        #--------------------------------------------------------
        # Calculations tab
    
        # Create label for standardization of NaOH calculations
        self.NaOH_Label = ttk.Label(self.calcs, text = 'Standardization of NaOH', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 21, font = self.font1).grid(row = 0, column = 1, columnspan = 1, pady = (15, 5))
        
        self.trial_Label = ttk.Label(self.calcs, text = 'Enter moles KHP and NaOH Molarity for Each Trial', background = 'blue', foreground = "blue", 
            relief = RAISED, anchor = CENTER, width = 45, font = self.font2).grid(row = 1, column = 1, columnspan = 1, pady = (15, 5))
            
        # Create entry boxes for moles khp 
        self.M1 = StringVar()
        self.M1_label = ttk.Label(self.calcs, text = 'Trial 1', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 13, font = self.font2)
        self.M1_label2 = ttk.Label(self.calcs, text = 'KHP:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 5, font = self.font2)
        self.M1_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M1)
        self.M1_label.grid(row = 2, column = 0, pady = (10, 5), sticky = 'e')
        self.M1_label2.grid(row = 3, column = 0, pady = (1, 5), sticky = 'w')
        self.M1_entry.grid(row = 3, column = 0, pady = (1, 5), sticky = 'e')
        self.M1.set('1.22')   
        
        self.M2 = StringVar()
        self.M2_label = ttk.Label(self.calcs, text = 'Trial 2', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.M2_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M2)
        self.M2_label.grid(row = 2, column = 1, pady = (10, 5))
        self.M2_entry.grid(row = 3, column = 1, pady = (1, 5))
        self.M2.set('2.54')  
            
        self.M3 = StringVar()
        self.M3_label = ttk.Label(self.calcs, text = 'Trial 3', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 15, font = self.font2)
        self.M3_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.M3)
        self.M3_label.grid(row = 2, column = 2, pady = (10, 5))
        self.M3_entry.grid(row = 3, column = 2, pady = (1, 5))
        self.M3.set('4.76')      
        
         # Create entry boxes for NaOH molarities
        self.Na1 = StringVar()
        self.Na1_label = ttk.Label(self.calcs, text = 'NaOH:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 6, font = self.font2)
        self.Na1_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.Na1)
        self.Na1_label.grid(row = 4, column = 0, pady = (1, 5), sticky = 'w')
        self.Na1_entry.grid(row = 4, column = 0, pady = (1, 5), sticky = 'e')
        self.Na1.set('1.22')   
        
        self.Na2 = StringVar()
        self.Na2_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.Na2)
        self.Na2_entry.grid(row = 4, column = 1, pady = (1, 5))
        self.Na2.set('2.54')  
            
        self.Na3 = StringVar()
        self.Na3_entry = ttk.Entry(self.calcs, width = 4, textvariable = self.Na3)
        self.Na3_entry.grid(row = 4, column = 2, pady = (1, 5))
        self.Na3.set('4.76')      
        
        
        # Enter boxes for average khp moles and NaOH molarity
        
        self.avg = StringVar()
        self.avg_label1 = ttk.Label(self.calcs, text = 'Enter Average Moles KHP and NaOH Molarity', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 40, font = self.font2)
        self.avg_label2 = ttk.Label(self.calcs, text = 'KHP:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 6, font = self.font2)
        self.avg_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.avg)
        self.avg_label1.grid(row = 5, column = 0, columnspan = 3, pady = (1, 5))
        self.avg_label2.grid(row = 6, column = 1, pady = (1, 5))
        self.avg_entry.grid(row = 7, column = 1, pady = (1, 5))
        self.avg.set('0.03')  
        
        self.naavg = StringVar()
        self.naavg_label1 = ttk.Label(self.calcs, text = 'NaOH:', background = 'blue', foreground = "blue", relief = RAISED, anchor = CENTER, width = 6, font = self.font2)
        self.naavg_entry = ttk.Entry(self.calcs, width = 6, textvariable = self.naavg)
        self.naavg_label1.grid(row = 8, column = 1, pady = (1, 5))
        self.naavg_entry.grid(row = 9, column = 1, pady = (1, 5))
        self.naavg.set('38.25')  
        
        
        # Create button that calls function for selecting files for analysis
        self.openFileButton = ttk.Button(self.calcs, text = 'Submit for Grading', style = "TButton", command = lambda: self.get_naoh_molarity_values())
        self.openFileButton.grid(row = 10, column = 1, pady = (1, 5))

            
    # Function to calculate molarity of NaOH in the standardization of NaOH experiment
    def get_naoh_molarity_values(self):
            
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
            
            
        # Check that all values are entered and are out to 2 decimal places
        # Place all values in a list
        values_list = [self.mass_khp1, self.mass_khp2, self.mass_khp3, self.vi1, self.vi2, self.vi3, 
            self.vf1, self.vf2, self.vf3, self.average, self.molarity1, self.molarity2, self.molarity3,
            self.avg_molarity]
                
        # Loop through list, convert to string, split the string around the decimal pt, and check for length
        # Start a list for yes/no depending on whether each value was entered correctly
        correct_list = []
        for val in values_list:
            y = str(val).split('.')
            if len(y[-1]) != 2:
                correct_list.append('no')
                    
            else:
                correct_list.append('yes')
                    
        # If list contains a no, go to error message
        if 'no' in correct_list:
            self.sigfig_error()
            
        else:
            self.calc_naoh_molarity()
            
        
    # Calculate average molarity based upon the khp masses and volumes entered in standardization of NaOH tab
    def calc_naoh_molarity(self):

        # Create lists for values so calculation can be run in a loop
        # Convert each element to float for calculations below
        self.mass_khp_list = [float(self.mass_khp1), float(self.mass_khp2), float(self.mass_khp3)]
        self.vi_list = [float(self.vi1), float(self.vi2), float(self.vi3)]
        self.vf_list = [float(self.vf1), float(self.vf2), float(self.vf3)]
        
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
        
        # Call grading function
        self.naoh_score()
        
       
    # Define a function that assigns points based upon correct calculation of moles khp and 
    # NaOH molarity entered
    # A correct response is one that is within 2% of the correct answer 
    def naoh_score(self):
        # Get student's average khp moles 
        self.student_khp = float(self.avg.get())
        
        # Compare with moles khp and NaOH molarity calculated based upon khp mass and volumes
        # Get calculated khp moles from rounded_moles_khp_list (use last entry in list)
        self.calculated_khp = self.rounded_moles_khp_list[-1]
        
        # Calculate 2% above and below the calculated_khp
        self.lower_khp = self.calculated_khp - 0.02*self.calculated_khp
        self.upper_khp = self.calculated_khp + 0.02*self.calculated_khp
        
        # Award 6 points for a correct response, 1 point for incorrect response
        if self.lower_khp < self.student_khp < self.upper_khp:
            self.khp_points = 6
            
        else:
            self.khp_points = 1
            
        print ('khp points = ' + str(self.khp_points))
        
        # Repeat for naoh
        self.student_naoh = float(self.naavg.get())
        self.calculated_naoh = self.rounded_naoh_molarity_list[-1]
        
        # Calculate 2% above and below the calculated_khp
        self.lower_naoh = self.calculated_naoh - 0.02*self.calculated_naoh
        self.upper_naoh = self.calculated_naoh + 0.02*self.calculated_naoh
        
        # Award 6 points for a correct response, 1 point for incorrect response
        if self.lower_naoh < self.student_naoh < self.upper_naoh:
            self.naoh_points = 6
            
        else:
            self.naoh_points = 1
            
        print ('NaOH points = ' + str(self.naoh_points))
        
    
    
    
    
#------------------------------------------------------------------------------------------------   
# Define error messages
       
    def sigfig_error(self):
        
        messagebox.showinfo('Message', 'Please fill in all entry boxes and make sure that all numbers are out to two decimal places.')
                        
            
        
       
            
            
            
        
#----------------------------------------------------------------------------------------------

# Execute application
# Create main page
root = tk.Tk()
b = titrate(root)
root.mainloop()




















