from flask import Flask
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    logout_user,
    current_user,
    UserMixin,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SECRET_KEY"] = "secret_key"

db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login/"


from .urls import *
