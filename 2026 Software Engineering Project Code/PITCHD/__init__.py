from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

"""
db = SQLAlchemy()
DB_name = "database.db"
"""

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lololol'
    
    from .page import page
    
    from .authentication import authentication
    
    app.register_blueprint(page, url_prefix = '/')
    app.register_blueprint(authentication, url_prefix = '/')    
    
    return app