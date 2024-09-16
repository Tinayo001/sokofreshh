#!/usr/bin/python3
# app/__init__.py

"""
This file contains the initialization code for our Flask application.
It sets up the application, configures extensions, and defines the application factory.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import config

"""
Initialize extensions
These extensions will be used throughout our application:
- db: Database management
- bcrypt: Password hashing
- jwt: JSON Web Token handling
- migrate: Database migration support
"""

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_name='default'):
    """
    Factory function to create and configure the Flask application
    
    Args:
        config_name (str): Name of the configuration to use. Defaults to 'default'.
    
    Returns:
        Flask: The configured Flask application instance
    """
    # Create the Flask application instance
    app = Flask(__name__, template_folder='templates', static_folder='static/')
    
    # Load the configuration based on the given name
    app.config.from_object(config[config_name])

    # Enable debug mode for development
    app.config['DEBUG'] = True

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Import routes and register them
    from app.routes import init_routes
    init_routes(app)

    return app

# Create the app instance
app = create_app()

