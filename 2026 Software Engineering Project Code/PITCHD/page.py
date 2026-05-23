from flask import Blueprint, render_template
page = Blueprint("page", __name__)

@page.route('/')
def home():
    return render_template('landing.html')

@page.route('/')
def profile():
    return render_template('profile.html')

