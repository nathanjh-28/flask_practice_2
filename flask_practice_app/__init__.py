from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key
app.config['SECRET_KEY'] = 'SAPNgFaCXp6CZTjq'

# db declaration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# from models import User, Post
from flask_practice_app import routes
