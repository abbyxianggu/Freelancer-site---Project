from flask import Blueprint, render_template, request, flash, redirect, url_for
from .database import User
from .import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import datetime

authentication = Blueprint("authentication", __name__)

# login route
@authentication.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for("page.profile"))
            else:
                flash("Incorrect password, try again.", category='error')
        else:
            flash("Email does not exist.", category='error')
    return render_template("login.html", user=current_user)

@authentication.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("authentication.login"))

@authentication.route("/sign_up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password1 = request.form["password"]
        password2 = request.form["confirm_password"]
        username = request.form["username"]
        print(f"EMAIL: {email}")
        print(f"PASSWORD: {password1} {password2}")
        if (len(password1) < 6):
            flash("password issue", category='error')
        elif len(email) < 4:
            flash("Email must be longer than 4 characters", category='error')  
        elif User.query.filter_by(username=username).first():
            flash("Username already exists", category='error')
        elif User.query.filter_by(email=email).first():
            flash("Email already exists", category='error')
        else:
            flash("Account created!", category='success')
            print(request.form["is_freelancer"])
            is_freelancer = False
            if request.form["is_freelancer"] != "None":
                is_freelancer = True
               
            new_user = User(
                username = request.form["username"],
                firstname = request.form["firstname"],
                lastname = request.form["lastname"],
                description = "UNSPECIFIED",
                email = request.form["email"],
                password = generate_password_hash(password1),
                date_of_birth = datetime.datetime.strptime(request.form["dob"], "%Y-%m-%d").date(),
                is_freelancer = False
            )
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for("page.profile"))
            
        # else we just enter the request
    
    return render_template('sign_up.html', user=current_user)

@authentication.route("/post_job")
def postjob():
    users=User.query.all()
    return render_template('post_job.html', user=current_user, users=users)

@authentication.route("/find_freelancer")
def findfreelancer():
    return render_template('find_freelancer.html', user=current_user)

@authentication.route("/find_work")
def findwork():
    return render_template('find_work.html', user=current_user)


