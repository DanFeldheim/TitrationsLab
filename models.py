from titrations_flask import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now)
    
    def __repr__(self):
        return "User('{self.username}', '{self.email}')"