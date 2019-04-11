import requests,json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='./templates')
#secrets.token_hex(16)
app.config['SECRET_KEY']='d5b14fc171f2e21be0907e9ba787b728'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from main import routes