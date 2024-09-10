#!/usr/bin/python3
# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import config

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

app = Flask(__name__, template_folder='frontend/templates')
app = Flask(__name__, static_folder='frontend/static/images')

from app.routes import init_routes
init_routes(app)

def create_app(config_name='default'):
    """Factory function to create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions with the app
    db.init_app(app)

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import routes and register them
    from app.routes import init_routes
    init_routes(app)

    return app

migrate = Migrate()

app = create_app()
migrate.init_app(app, db)

