from flask import Flask
import os
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# db.init_app(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

