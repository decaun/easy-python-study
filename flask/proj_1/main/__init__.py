import requests,json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, template_folder='./templates')
#secrets.token_hex(16)
app.config['SECRET_KEY']='d5b14fc171f2e21be0907e9ba787b728'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
login_manager=LoginManager(app)

from main import routes