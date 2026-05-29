from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os 

db = SQLAlchemy()
DB_name = "database.db"


def create_app():
    app = Flask(__name__)
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    app.config['SECRET_KEY'] = 'lololol'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(app.instance_path, DB_name)
    
    db.init_app(app)
    
    from .page import page
    
    from .authentication import authentication
    
    app.register_blueprint(page, url_prefix = '/')
    app.register_blueprint(authentication, url_prefix = '/')    
    
    from .database import User, Task
    create_database(app)
    #login manager
    login_manager = LoginManager()
    login_manager.login_view = "authentication.login"
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


def create_database(app):
    if not os.path.exists(os.path.join(app.instance_path, DB_name)):
        with app.app_context():
            db.create_all()
        print("created database")