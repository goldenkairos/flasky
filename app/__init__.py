from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/breakfasts_development'
    app.config['SQLALCHEMY_ECHO'] = True
    
    db.init_app(app) #connecting database
    migrate.init_app(app,db) #migration in our database
    
    from app.models.breakfast import Breakfast #importing model Breakfast into our project. This line of code can be anywhere
    
    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)
    return app