from.import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True)
    email = db.Column(db.String(150), unique = True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    description = db.Column(db.String(500))
    password = db.Column(db.String(150))
    date_of_birth = db.Column(db.Date)
    is_freelancer = db.Column(db.Boolean, default=False, nullable=False)
    contact_email = db.Column(db.String(150))
    contact_phone = db.Column(db.String(20))
    payment_method = db.Column(db.String(100))
    payment_details = db.Column(db.String(200))
    

class Task (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(1000))
    occupied = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)