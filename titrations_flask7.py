from flask import Flask, render_template, flash, request, url_for, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, FloatField, SelectField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import csv


app = Flask(__name__)

# Create a secret key for the users db
app.config['SECRET_KEY'] = 'mysecretkey$%030667'

# Create sql database for user info
# This database has a column for user role. It automatically populates as student, but can be changed to admin manually.
# If set to admin in sql, that user will have access to student info in flask.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Create a 2nd database for grades 
app.config['SQLALCHEMY_BINDS'] = {'grades': 'sqlite:///grades.db'}
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Set up SQLite database for student information
# Could also import models.py instead
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(15), nullable = False)
    # date_created = db.Column(db.DateTime, default = datetime.now)
    date_created = db.Column(db.DateTime, index = False, unique = False, nullable = False)
    # Create a user role column that is hardcoded to 'student' below
    # An admin can be set by manually entering users.db and changing the user_role column to admin
    user_role = db.Column(db.String(8))
    
    # Function for specifying how user objects are printed out
    def __repr__(self):
        return "User('{self.username}', '{self.email}')"
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
# Set up SQLite database for student grades
class Grades(db.Model):
    __bind_key__ = 'grades'
    id = db.Column(db.Integer, primary_key = True)
    time = db.Column(db.String)
    student_username = db.Column(db.String)
    student_email = db.Column(db.String)
    molesKHP = db.Column(db.Integer)
    NaOH = db.Column(db.Integer)
    pKa = db.Column(db.Integer)
    acid = db.Column(db.Integer)
    total_pts = db.Column(db.Integer)
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email(message = 'Invalid email'), Length(max = 50)])
    # Max is 80 for hashing
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8, max = 80)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
class loginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email(message = 'Invalid email'), Length(max = 50)])
    username = StringField('Username', validators = [DataRequired(), Length(min = 4, max = 15)])
    password = PasswordField('Password', validators = [DataRequired()]) 
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class DataForm(FlaskForm):

    # Variables for NaOH standardization
    khp1 = StringField('khp1', validators = [DataRequired()])
    khp2 = StringField('khp2', validators = [DataRequired()])
    khp3 = StringField('khp3', validators = [DataRequired()])
    initvol1 = StringField('initvol1', validators = [DataRequired()])
    initvol2 = StringField('initvol2', validators = [DataRequired()])
    initvol3 = StringField('initvol3', validators = [DataRequired()])
    finalvol1 = StringField('finalvol1', validators = [DataRequired()])
    finalvol2 = StringField('finalvol2', validators = [DataRequired()])
    finalvol3 = StringField('finalvol3', validators = [DataRequired()])
    
    # Variables for unknown acid titration
    voltitrated = StringField('voltitrated', validators = [DataRequired()])
    unknown_acid = StringField('unknown', validators = [DataRequired()])
    init_buret = StringField('initburet', validators = [DataRequired()])
    final_buret = StringField('finalburet', validators = [DataRequired()])
    quarter_pt = StringField('quarter', validators = [DataRequired()])
    half_pt = StringField('half', validators = [DataRequired()])
    threeQuarter_pt = StringField('threeQuarter', validators = [DataRequired()])
    equiv_volume = StringField('equivVolume', validators = [DataRequired()])
    
    # Student calculations
    studentMolesKHP1 = StringField('studentkhp1', validators = [DataRequired()])
    studentMolesKHP2 = StringField('studentkhp2', validators = [DataRequired()])
    studentMolesKHP3 = StringField('studentkhp3', validators = [DataRequired()])
    studentNaohMolarity1 = StringField('studentnaohmolarity1', validators = [DataRequired()])
    studentNaohMolarity2 = StringField('studentnaohmolarity2', validators = [DataRequired()])
    studentNaohMolarity3 = StringField('studentnaohmolarity3', validators = [DataRequired()])
    studentAverageNaohMolarity = StringField('Average NaOH Molarity', validators = [DataRequired()])
    studentColorEndpointMolarity = StringField('Acid Molarity Based Upon the Color Endpoint', validators = [DataRequired()])
    studentAccurateEndpointMolarity = StringField('Acid Molarity Based Upon the Accurate pH Titration', validators = [DataRequired()])
    studentQuarterPointpK = StringField('pKa from the 1/4 Equivalence Volume', validators = [DataRequired()])
    studentHalfPointpK = StringField('pKa from the 1/2 Equivalence Volume', validators = [DataRequired()])
    studentThreeQuarterPointpK = StringField('pKa from the 3/4 Equivalence Volume', validators = [DataRequired()])
    studentAveragepK = StringField('Average pKa', validators = [DataRequired()])
    
    # Button to grade assignment
    submit4 = SubmitField()
    
# Download grades in csv format
# Links to button in instructors.html
# Allows people with admin roles to access grades and student responses    
@app.route('/return_file/', methods = ['GET', 'POST'])
def download_file():

    return send_file('/Users/danfeldheim/Documents/GitHub/Auto_Lab_Graders/TitrationsLab/titrationslabscores.csv', attachment_filename = 'titrationslabscores.csv')
    
# Download student responses in csv format
# Links to button in instructors.html    
@app.route('/student_responses/', methods = ['GET', 'POST'])
def download_responses():
     
    return send_file('/Users/danfeldheim/Documents/GitHub/Auto_Lab_Graders/TitrationsLab/titrationslab_student_responses.csv', attachment_filename = 'titrationslabstudent_responses.csv') 
                    
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Add 'student' to user_role column of users.db as a default
        # Enter users.db manually to change the user role to admin
        role = 'student'
        # Hash the password
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_password, 
            date_created = datetime.now(), user_role = role)
        db.session.add(new_user)
        db.session.commit()
        
        # Can't get flash to work so replaced with a link. 
        flash('Account created!')
        return '<h1 style = "color:blue;">Registration Successful!</h1>'
        # return redirect(url_for('login'))
        
    return render_template('register.html', title = 'Register', form = form)
      
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        
        # Check if username was entered correctly so we can use it to populate grade book and student response db
        if db.session.query(User.id).filter_by(username = form.username.data).scalar() is not None:
        
            # Filter the db by username
            user = User.query.filter_by(username = form.username.data).first()
            
            # Check if the user is admin
            # Get user_role
            role = User.query.filter_by(username = form.username.data).first().user_role
            
            # If password was correct, check the role
            if check_password_hash(user.password, form.password.data):
                if role == 'admin':
                    # Create a variable for username (called student_username even though it's for the instructor). This gets populated in a table 
                    # displayed in instructors.html page.
                    student_username = form.username.data
                    # Get all users in db to display in table that can admin can access
                    students = User.query.all()
    
                    # Pass username and list of students to instructors.html
                    return render_template('instructors.html', title = 'Instructors', name = student_username, students = students)
                
                # Do this if user is not admin    
                else: 
                    login_user(user, remember = form.remember.data)
                    
                    # Create a global for the student's email for use in the final grade sheet
                    global student_email
                    student_email = form.email.data
                        
                    # Create a global for student's username for use in the final grade sheet
                    global student_username
                    student_username = form.username.data
                        
                    return redirect(url_for('data'))
                
            # If password was incorrect
            else:
                return "<h1 style = 'color:blue;'>Invalid password</h1>"
        
        # If username was incorrect        
        else:
            return "<h1 style = 'color:blue;'>Invalid username</h1>"
   
       
    return render_template('login.html', title = 'Login', form = form)
    
# Create logout function
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Send to a 'you have been logged out page' 
    # return "<h1 style = 'color:blue;'>You have been logged out.</h1>"
    return render_template('logout_message.html')
    
    # Could also just redirect back to the login page
    # return redirect(url_for('login'))
    
@app.route('/enter_calculations', methods = ['Get', 'POST'])
@login_required
def data():
    
    form = DataForm()
    
    # Get the date and time answered were submitted
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get data entered into standardization of NaOH table
    khp1 = form.khp1.data
    khp2 = form.khp2.data
    khp3 = form.khp3.data
    initvol1 = form.initvol1.data
    initvol2 = form.initvol2.data
    initvol3 = form.initvol3.data
    finalvol1 = form.finalvol1.data
    finalvol2 = form.finalvol2.data
    finalvol3 = form.finalvol3.data
    
    # Get data entered into unkown acid table
    voltitrated = form.voltitrated.data
    unknown_acid = form.unknown_acid.data
    init_buret = form.init_buret.data
    final_buret = form.final_buret.data
    quarter_pt = form.quarter_pt.data
    half_pt = form.half_pt.data
    threeQuarter_pt = form.threeQuarter_pt.data
    equiv_volume = form.equiv_volume.data
    
    # Get data from student calculations table
    studentMolesKHP1 = form.studentMolesKHP1.data
    studentMolesKHP2 = form.studentMolesKHP2.data
    studentMolesKHP3 = form.studentMolesKHP3.data
    studentNaohMolarity1 = form.studentNaohMolarity1.data
    studentNaohMolarity2 = form.studentNaohMolarity2.data
    studentNaohMolarity3 = form.studentNaohMolarity3.data
    studentAverageNaohMolarity = form.studentAverageNaohMolarity.data
    studentColorEndpointMolarity = form.studentColorEndpointMolarity.data
    studentAccurateEndpointMolarity = form.studentAccurateEndpointMolarity.data
    studentQuarterPointpK = form.studentQuarterPointpK.data
    studentHalfPointpK = form.studentHalfPointpK.data
    studentThreeQuarterPointpK = form.studentThreeQuarterPointpK.data
    studentAveragepK = form.studentAveragepK.data
    
    # Create lists to be checked for significant figures
    # Place 2-decimal data into list (pK data) for sig fig check
    two_decimals_list = [initvol1, initvol2, initvol3, finalvol1, finalvol2, finalvol3, voltitrated, 
                    init_buret, final_buret, quarter_pt, half_pt, threeQuarter_pt, equiv_volume, studentQuarterPointpK, 
                    studentHalfPointpK, studentThreeQuarterPointpK, studentAveragepK]
    
    # Place 4-decimal data into list
    four_decimals_list = [khp1, khp2, khp3, studentNaohMolarity1, studentNaohMolarity2, studentNaohMolarity3, studentAverageNaohMolarity,
                        studentColorEndpointMolarity, studentAccurateEndpointMolarity]  
                                           
    # Place 6-decimal data into list
    six_decimals_list = [studentMolesKHP1, studentMolesKHP2, studentMolesKHP3]
    
    # When student submits data, do this           
    if 'submit4' in request.form:
        
        # Call functions that check for sig figs
        x = two_sig_figs(two_decimals_list)
        y = four_sig_figs(four_decimals_list)
        z = six_sig_figs(six_decimals_list)
        
        # If any entry had incorrect number of sig figs, throw error
        if x == 'no' or y == 'no' or z == 'no':
            
            return redirect(url_for('error'))
            
        else:
            # Combine lists
            data_list = two_decimals_list + four_decimals_list + six_decimals_list
            
            # Create a student response list of student_username + data_list, studentAssignedAcid, studentPredictedAcid, and '\n' 
            # to write each response in a new row in excel file
            # Get assigned and predicted acids from dropdown menus (Can't do this above with the others for some reason.)
            studentAssignedAcid = request.form['assigned']
            studentPredictedAcid = request.form['predicted']
            
            # Copy data_list
            student_response_list = list(data_list)
            # Insert student username at the beginning of list
            student_response_list.insert(0, student_username)
            
            # Append 
            student_response_list.append(studentAssignedAcid)
            student_response_list.append(studentPredictedAcid)
            
            # Insert datatime at end
            student_response_list.append(date_time)
            
            # Insert a return to ensure that next entry goes in the next row
            student_response_list.append('\n')
            
            # Export data_list to csv file
            response_csvFile = "/Users/danfeldheim/Documents/GitHub/Auto_Lab_Graders/TitrationsLab/titrationslabstudent_responses.csv"
            
            with open(response_csvFile, "a") as f:
                
                wr = csv.writer(f, dialect = 'excel')
                # This hack appears to ensure that the new row gets appended directly under the last row
                wr.writerow([])
                wr.writerow(student_response_list)
            
            
            # Call functions to calculate correct answers bases upon student data
            # Call calculate_moles_khp() for calculating correct moles khp based upon student entries
            correct_moles_khp_list = calculate_moles_khp(data_list)
            
            # Call calculate_NaOH_molarity calcs
            # Pass correct_moles_khp_list to use khp masses
            correct_NaOH_molarity_list = calculate_NaOH_molarity(data_list, correct_moles_khp_list, studentNaohMolarity1, studentNaohMolarity2, studentNaohMolarity3)
            correct_avg_naoh_molarity = correct_NaOH_molarity_list[-1]
            
            return render_template(str(correct_avg_naoh_molarity))
            
            # Call acid_molarity_calc for color endpoint calcs
            acid_molarity = acid_molarity_calc(data_list)
            
            # Call pka_calcs for pH titration calculations
            pKa_list = pKa_calcs(data_list, quarter_pt, half_pt, threeQuarter_pt)
             
            
            # Call scoring functions to award points. These compare student calculations to correct calculations
            # Get the number of pts for pKa entries (2 pts/correct response)
            pKa_pts = pKa_score(pKa_list, studentQuarterPointpK, studentHalfPointpK, studentThreeQuarterPointpK, studentAveragepK)
            
            # Get the number of points for khp moles entered by student
            khp_pts = khp_score(studentMolesKHP1, studentMolesKHP2, studentMolesKHP3, correct_moles_khp_list)
          
            # Get the number of points for avg naoh molarity entered by student
            naoh_pts = naoh_score(studentAverageNaohMolarity, correct_avg_naoh_molarity)
            
            # Calculated pts for predicted acid
            acid_prediction_pts = acid_prediction(studentPredictedAcid, studentAssignedAcid)
            
            # Add up points earned
            total = khp_pts + naoh_pts + pKa_pts + acid_prediction_pts
            
            # Generate a sql database of student grades
            # This must go before calling the grading summary function because that function opens a new html page
            # and the program stops at that point.
            points_earned = Grades(time = date_time, student_username = student_username, student_email = student_email, molesKHP = khp_pts, NaOH = naoh_pts,
                                pKa = pKa_pts, acid = acid_prediction_pts, total_pts = total)
                                
            db.session.add(points_earned)
            db.session.commit()
            
            # Count the number of student submissions from grades.db 
            grades_data = Grades.query.filter_by(student_username = student_username).count()
            
            submissions_remaining = 5 - grades_data
            
            # Call grading_summary function for a complete summary of points
            return grading_summary(student_username, pKa_pts, khp_pts, naoh_pts, acid_prediction_pts, submissions_remaining)
               
  
    # Render the page
    return render_template('titrations_all_in_one.html', title = 'Titrations Lab', form = form, name = current_user.username)
    


# Create popup messages
@app.route('/sigfigerror')
def error():
    return render_template('sigfigerrormessage.html') 
    
@app.route('/correctsigfigs')
def correct():
    return render_template('correctsigfigs.html')
      
# Functions to check for sig figs of student entries
def two_sig_figs(two_decimals_list):
    
    # If NA in list, delete it
    while 'NA' in two_decimals_list: 
        two_decimals_list.remove('NA')
        
    # Loop through list, split the string around the decimal pt, and check for length
    # Check for '.' first 
    # Start a list for yes/no depending on whether each value was entered correctly
    correct_list1 = []
    for val in two_decimals_list:
        if '.' in val:
            y = val.split('.')
            if len(y[-1]) != 2:
                correct_list1.append('no')
                        
            else:
                correct_list1.append('yes')
        else:
            correct_list1.append('no')
        
    # If list contains a no, return 'no'
    # Also return list1 for student calculations tables
    if 'no' in correct_list1:
            
        x = 'no'
        return (x)
            
    else:
             
        x = 'yes'
        return (x)
        
  
def four_sig_figs(four_decimals_list):
    
    # If NA in list, delete it
    while 'NA' in four_decimals_list: 
        four_decimals_list.remove('NA')
    
    correct_list2 = []
    for entry in four_decimals_list:
        if '.' in entry:
            y = entry.split('.')
            
            if len(y[-1]) != 4:
                correct_list2.append('no')
                        
            else:
                correct_list2.append('yes')
        else:
            correct_list2.append('no')
        
    # If list contains a single no return no as list2
    # Used in student calculations tables
    
    if 'no' in correct_list2:
            
        y = 'no'
        return (y)
            
    else:
            
        y = 'yes'
        return (y)
        
        
def six_sig_figs(six_decimals_list):
    
    # If NA in list, delete it
    while 'NA' in six_decimals_list: 
        six_decimals_list.remove('NA')
    
    correct_list3 = []
    for entry in six_decimals_list:
        if '.' in entry:
            z = entry.split('.')
            if len(z[-1]) != 6:
                correct_list3.append('no')
                        
            else:
                correct_list3.append('yes') 
        else:
           correct_list3.append('no')  
            
    # If list contains a single no return no as list2
    # Used in student calculations tables
    
    if 'no' in correct_list3:
            
        z = 'no'
        return (z)
            
    else:
            
        z = 'yes'
        return (z)    

                                                               
# Functions to calculate correct answers
def calculate_moles_khp(data_list):
    
    # Calculate moles khp from student's mass khp
    # Extract mass khp from data_list
    khp1 = data_list[17]
    khp2 = data_list[18]
    khp3 = data_list[19]
    
    # Create list for khp masses
    mass_khp_list = [khp1, khp2, khp3]
      
    # Create list for results
    correct_moles_khp_list = []
        
    for mass in mass_khp_list:
        
        # Just in case an entry was skipped by student    
        if mass == 'NA':
            correct_moles_khp_list.append('NA')
                
        else:    
            # Convert mass to float
            mass = float(mass)
          
            # Calculate moles and append result to list
            moles_khp = mass/204.22
            correct_moles_khp_list.append(moles_khp)
                           
    return (correct_moles_khp_list)

   
def calculate_NaOH_molarity(data_list, correct_moles_khp_list, studentNaohMolarity1, studentNaohMolarity2, studentNaohMolarity3):

    # Build student's volume lists
        initvol1 = data_list[0]
        initvol2 = data_list[1]
        initvol3 = data_list[2]
        finalvol1 = data_list[3]
        finalvol2 = data_list[4]
        finalvol3 = data_list[5]
        
        vi_list = [initvol1, initvol2, initvol3] 
        vf_list = [finalvol1, finalvol2, finalvol3]
        
        # Calculate NaOH molarity for each trial and then average
        # Calculate Vf - Vi for each element in vi_list and vf_list and add to list
        
        # Create a volume difference list
        vol_diff_list = []
        
        for initial_vol, final_vol in zip(vi_list, vf_list):
            
            if initial_vol == 'NA' or final_vol == 'NA':
                vol_diff_list.append('NA')
                
            else:
                # Convert to float
                initial_vol = float(initial_vol)
                final_vol = float(final_vol)
                
                # Take difference
                vol_diff = final_vol - initial_vol
                vol_diff_list.append(vol_diff)
                
        
        # Use zip to grab corresponding elements from vol and moles lists and calculate NaOH molarity for each trial
        # Create a molarity list for results
        naoh_molarity_list = []
        
        for moles, vol in zip(correct_moles_khp_list, vol_diff_list):
            
            # If an element in either list contains NA, move on.
            if moles == 'NA' or vol == 'NA':
                
                naoh_molarity_list.append('NA')
                            
            else:
            
                molarity = 1000*(moles/vol)
                naoh_molarity_list.append(molarity)    
                    
        # Calculate average and append to list
        # Need to remove NA from list first
        avg_naoh_list = naoh_molarity_list
        
        # If NA was entered in one of the calculated NaOH Molarity boxes, change the entry in avg_naoh_list to NA
        # Create list from student molarities
        studentNaohMolarity_list = [studentNaohMolarity1, studentNaohMolarity2, studentNaohMolarity3]
        
        # Check for NA and return index location if found
        if 'NA' in studentNaohMolarity_list:
            location = studentNaohMolarity_list.index('NA')
            
            # Change the same index location in avg_naoh_list to NA
            avg_naoh_list[location] = 'NA'
        
        while 'NA' in avg_naoh_list: 
            avg_naoh_list.remove('NA')
            
        avg_naoh_molarity = sum(avg_naoh_list)/len(avg_naoh_list)
        
        # Append the average to the original list self.naoh_molarity_list
        naoh_molarity_list.append(avg_naoh_molarity)
        
        correct_NaOH_molarity_list = naoh_molarity_list
        
        return (correct_NaOH_molarity_list)
        
        
        # Round values to 6 decimal places
        # self.rounded_naoh_molarity_list = [round(i, 6) for i in self.naoh_molarity_list]
            
# Acid molarity
def acid_molarity_calc(data_list):
            
    # Get initial and final buret volumes, and volume titrated from data_list
    vol_titrated = data_list[6]
    init_buret = data_list[7]
    final_buret = data_list[8]
    
    # Get average moles NaOH entered by student
    avg_moles_naoh = data_list[23]
    
    # Formula: mols acid/vol of acid titrated 
    # and mols acid = self.buret2 - self.buret1 * self.avg_naoh_molarity * 0.001
      
    acid_mols = (float(init_buret) - float(final_buret)) * float(avg_moles_naoh) * 0.001
    acid_molarity = float(acid_mols)/float(vol_titrated)
            
    return (acid_molarity)       

# Calculate pKa from pH values entered by student at different volumes in the pH titration    
def pKa_calcs(data_list, quarter_pt, half_pt, threeQuarter_pt):
    
        # Create list for pKa calculations
        pKa_list = []
        
        if quarter_pt != 'NA':
            pK1 = float(quarter_pt) + 0.477
            pKa_list.append(pK1)
            
        else:
            pK1 = 'NA'
            pKa_list.append(pK1)
             
        if half_pt != 'NA':
            pK2 = float(half_pt)
            pKa_list.append(pK2)
        
        else:
            pK2 = 'NA'
            pKa_list.append(pK2)
            
                  
        if threeQuarter_pt != 'NA':
            pK3 = float(threeQuarter_pt) - 0.477
            pKa_list.append(pK3)
            
        else:
            pK3 = 'NA'
            pKa_list.append(pK3)
            
        # Remove NA so average pKa can be calculated
        # Make a copy
        pKa_list_noNA = pKa_list
        while 'NA' in pKa_list_noNA:
            pKa_list_noNA.remove('NA') 
        
        # Calculate average 
        pKa_avg = sum(pKa_list_noNA)/len(pKa_list_noNA)
        
        # Append pKa_avg to pKa_list and return
        pKa_list.append(pKa_avg)
        
        return pKa_list
            

# Scoring functions

# Function to calculate points for student pKa values  
def pKa_score(pKa_list, studentQuarterPointpK, studentHalfPointpK, studentThreeQuarterPointpK, studentAveragepK):
    
    
    # Build a list of pKa values entered by student
    student_pKa_list = [studentQuarterPointpK, studentHalfPointpK, studentThreeQuarterPointpK, studentAveragepK]
    
    # Start counter for khp points
    pKa_pts = 0
        
    # Create list for correct vs incorrect pKa responses
    number_correct_pK = []
        
    for student_pK, correct_pK in zip(student_pKa_list, pKa_list):
                
        # If either list has NA move on
        if student_pK == 'NA' or correct_pK == 'NA':
                pass
                             
        else:
            # Convert student_pK to float
            student_pK = float(student_pK)
                
            # Convert correct_pK to float
            correct_pK = float(correct_pK)
            
            # Set upper and lower limits for correct answer
            upper_pK = round(correct_pK + (0.02 * correct_pK), 2)
            lower_pK = round(correct_pK - (0.02 * correct_pK), 2)
            
            if upper_pK >= student_pK >= lower_pK:
                pKa_pts += 2
                number_correct_pK.append('correct')
                        
            else:
                number_correct_pK.append('incorrect')
                    
    return pKa_pts  
 
# Function to grade moles khp entered by students
def khp_score(studentMolesKHP1, studentMolesKHP2, studentMolesKHP3, correct_moles_khp_list):
            
    # Build list of moles khp entered by student
    student_moles_khp_list = [studentMolesKHP1, studentMolesKHP2, studentMolesKHP3]
           
    # Award 2 points for a each correct response         
    # Start counter for khp points
    khp_pts = 0
        
    # Create list to track correct vs incorrect responses
    number_correct_khp = []
           
    for student_moles_khp, correct_moles_khp in zip(student_moles_khp_list, correct_moles_khp_list):
            
        if student_moles_khp == 'NA' or correct_moles_khp == 'NA':
            pass
                
        else:
                
            # Convert student_moles_khp and correct_moles_khp to float
            student_moles_khp = float(student_moles_khp)
            correct_moles_khp = float(correct_moles_khp)
                
            # Set upper and lower limits for correct answer
            upper_khp = correct_moles_khp + (0.02 * correct_moles_khp)
            lower_khp = correct_moles_khp - (0.02 * correct_moles_khp)
                
            if upper_khp >= student_moles_khp >= lower_khp:
                khp_pts += 2
                # Append correct to list
                number_correct_khp.append('correct')
                        
            else:
                # Append incorrect to list
                number_correct_khp.append('incorrect')
                                       
    return khp_pts
    
    
def naoh_score(studentAverageNaohMolarity, correct_avg_naoh_molarity):
    
    # Start counter for NaOH points
    naoh_pts = 0
            
    # Calculate 2% above and below the calculated average naoh molarity
    lower_naoh = float(correct_avg_naoh_molarity) - (0.02 * float(correct_avg_naoh_molarity))
    upper_naoh = correct_avg_naoh_molarity + (0.02 * correct_avg_naoh_molarity)
            
    # Award 6 points for a correct response, 1 point for incorrect response
    if float(lower_naoh) < float(studentAverageNaohMolarity) < float(upper_naoh):
        
        naoh_pts = 6
                     
             
    return naoh_pts      
    
def acid_prediction(studentPredictedAcid, studentAssignedAcid):
    
# Get unkown from drop-down menu (A-F) and assign an acid   
            
    if studentPredictedAcid == 'Acetic' and (studentAssignedAcid == 'A' or studentAssignedAcid == 'D'):
            
        acid_prediction_pts = 5
                
    elif studentPredictedAcid == 'Carbonic' and (studentAssignedAcid == 'B' or studentAssignedAcid == 'E'):
        
        acid_prediction_pts = 5
        
    elif (studentPredictedAcid == 'Propionoic' and (studentAssignedAcid == 'C' or studentAssignedAcid == 'F')):
        
        acid_prediction_pts = 5
        
    else:
        
        acid_prediction_pts = 0
        
        
    return acid_prediction_pts
    

@app.route('/scores', methods = ['GET', 'POST'])
# Pass all points to grading summary
def grading_summary(student_username, pKa_pts, khp_pts, naoh_pts, acid_prediction_pts, submissions_remaining):
    
    total_score = str(pKa_pts + khp_pts + naoh_pts + acid_prediction_pts)
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Export scores to csv file
    csvRow = [date_time, student_username, pKa_pts, khp_pts, naoh_pts, acid_prediction_pts, total_score, '\n']
    csvFile = "/Users/danfeldheim/Documents/GitHub/Auto_Lab_Graders/TitrationsLab/titrationslabscores.csv"
    with open(csvFile, "a") as f:
        
        wr = csv.writer(f, dialect = 'excel')
        # This hack appears to ensure that each new row is appended directly under the last row
        wr.writerow([])
        wr.writerow(csvRow)
        
    # If number of submissions = 5, automatically logout student and display grade table
        if submissions_remaining == 0:
            # Automatically logout user and display grade summary
            logout_user()
            return render_template('titrations_lab_no_submissions.html', pKa_pts = pKa_pts, khp_pts = khp_pts, naoh_pts = naoh_pts, acid_prediction_pts = acid_prediction_pts, 
                        submissions_remaining = submissions_remaining, title = 'Scoring Summary') 
            
        else:    
            # Pass all points to gradedanswers.html for display in table
            return render_template('gradedanswers.html', pKa_pts = pKa_pts, khp_pts = khp_pts, naoh_pts = naoh_pts, acid_prediction_pts = acid_prediction_pts, 
                        submissions_remaining = submissions_remaining, title = 'Scoring Summary') 
            
    
    
    
    
if __name__ == "__main__":
    app.run(debug = True)