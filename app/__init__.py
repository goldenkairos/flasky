from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv #let us load data to the environment
import os #allow us to pull out of our enviroment


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(testing = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/breakfasts_development'
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_ECHO'] = True
    
    if testing is None: #if we don't do test, then we will pull data from normal database
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else: #if we test, then we will pull data from the testing database that we named in .env file
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
        
    db.init_app(app) #connecting database
    migrate.init_app(app,db) #migration in our database
    
    from app.models.breakfast import Breakfast #importing model Breakfast into our project. This line of code can be anywhere
    
    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)
    return app