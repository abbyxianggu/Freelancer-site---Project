from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

db = SQLAlchemy()
DB_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lololol'
    app.config['SQL_ALCHEMY_DATABASE_URI'] =f'sqlite://{DB_name}'
    
    db.init(app)
    
    from .page import page
    
    from .authentication import authentication
    
    app.register_blueprint(page, url_prefix = '/')
    app.register_blueprint(authentication, url_prefix = '/')    
    
    from .database import User, Task
    create_database(app)
    return app


def create_database(app):
    if not os.path.exists('/'+ DB_name):
        db.create_all(app=app)
        print("created database")