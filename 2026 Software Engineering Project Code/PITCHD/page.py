from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .import db
from .database import User, Task

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
        current_user.contact_email = request.form.get("contact_email", "")
        current_user.contact_phone = request.form.get("contact_phone", "")
        current_user.payment_method = request.form.get("payment_method", "")
        current_user.payment_details = request.form.get("payment_details", "")
        db.session.commit()
        return redirect(url_for("page.profile"))
    tasks_accepted = Task.query.filter_by(worker_id = current_user.id)
    tasks_posted = Task.query.filter_by(user_id = current_user.id)
    return render_template('profile.html', user=current_user, tasks_accepted=tasks_accepted, tasks_posted=tasks_posted)



