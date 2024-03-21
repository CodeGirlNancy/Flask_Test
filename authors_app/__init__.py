from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extensions import db 
from authors_app.extensions import migrate  # Removed duplicate import of Migrate

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)  # Use Migrate from flask_migrate to initialize migrations

    # Importing and registering models
    from authors_app.models.user import User
    from authors_app.models.company import Company
    from authors_app.models.books import Books

    @app.route('/')
    def home():
        return "Authors App API setup"

    return app

