from.import db
from flask_login import UserMixin

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    description = db.Column(db.String(500))
    password = db.Column(db.String(150))
    date_of_birth = db.Column(db.Date)
    

class Task (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))