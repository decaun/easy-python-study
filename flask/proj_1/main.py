#$env:FLASK_APP=".\main.py"
#$env:FLASK_DEBUG=1
#$env:FLASK_RUN_PORT=80 - bi sike yaramadi
#flask run --host=127.0.0.1 --port=80
#python -m flask run --host=127.0.0.1 --port=5000
import requests,json
from datetime import datetime
from flask import Flask,render_template,jsonify,request,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./templates')
#secrets.token_hex(16)
app.config['SECRET_KEY']='d5b14fc171f2e21be0907e9ba787b728'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        username=db.Column(db.String(20),unique=True,nullable=False)
        email=db.Column(db.String(120),unique=True,nullable=False)
        password_token=db.Column(db.String(60),nullable=False)
        posts=db.relationship('Post',backref='author',lazy=True)

        def __repr__(self):
                return f"User('{self.username}','{self.email}','{self.password_token}')"

class Post(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        title=db.Column(db.String(100),primary_key=True)
        date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
        content=db.Column(db.Text,nullable=False)
        user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

        def __repr__(self):
                return f"User('{self.title}','{self.date_posted}')"

posts=[
    {
            'author':'ali',
            'title':'best playlist ever',
            'content':'check dis aut',
            'date_posted':'April 20,2019'
    },
    {
            'author':'veli',
            'title':'better playlist',
            'content':'check dis instead',
            'date_posted':'April 21,2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts_var=posts)

@app.route("/topic")
def topic():
    return render_template('topic.html',title_var='Topic#1')
    
    
if __name__=='__main__':
    app.run(debug=True)
    app.run(host = '127.0.0.1',port=80)
