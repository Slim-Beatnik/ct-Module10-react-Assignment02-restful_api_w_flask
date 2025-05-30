from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase
import os

# Initialize Flask app
app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<YOUR PASSWORD>@localhost/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating our Base Model
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy and Marshmallow
db = SQL
