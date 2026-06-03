from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from.import db
page = Blueprint("page", __name__)

@page.route('/')
def home():
    return render_template('landing.html', user=current_user)

@login_required
@page.route('/profile', methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        current_user.description = request.form["description"]
        is_freelancer = "freelancer" in request.form
        current_user.is_freelancer = is_freelancer
        db.session.commit()
        return redirect(url_for("page.profile"))
    return render_template('profile.html', user=current_user)



