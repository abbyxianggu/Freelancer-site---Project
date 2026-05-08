from flask import Blueprint, render_template

authentication = Blueprint("authentication", __name__)

@authentication.route("/login")
def login():
    return render_template('login.html')

@authentication.route("/logout")
def logout():
    return  render_template('logout.html')


@authentication.route("/sign_up")
def signup():
    return render_template('sign_up.html')

@authentication.route("/postjob")
def postjob():
    return render_template('postjob.html')

@authentication.route("/findfreelancer")
def findfreelancer():
    return render_template('findfreelancer.html')

@authentication.route("/findwork")
def findwork():
    return render_template('findwork.html')