"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """Connect db to Flask app"""
    db.app = app
    db.init_app(app)
