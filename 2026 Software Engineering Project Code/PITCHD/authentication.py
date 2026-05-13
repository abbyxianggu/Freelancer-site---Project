from flask import Blueprint, render_template, request, flash

authentication = Blueprint("authentication", __name__)

@authentication.route("/login")
def login():
    return render_template('login.html')

@authentication.route("/logout")
def logout():
    return  render_template('logout.html')

@authentication.route("/sign_up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password")
        password2 = request.form.get("confirm_password")
        print(f"EMAIL: {email}")
        print(f"PASSWORD: {password1} {password2}")
        if (len(password1) < 6):
            flash("password issue", category='error')
        # else we just enter the request
    
    return render_template('sign_up.html')

@authentication.route("/post_job")
def postjob():
    return render_template('post_job.html')

@authentication.route("/find_freelancer")
def findfreelancer():
    return render_template('find_freelancer.html')

@authentication.route("/find_work")
def findwork():
    return render_template('find_work.html')