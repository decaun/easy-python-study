#$env:FLASK_APP=".\main.py"
#$env:FLASK_DEBUG=1
#$env:FLASK_RUN_PORT=80 - bi sike yaramadi
#flask run --host=127.0.0.1 --port=5000
#python -m flask run --host=127.0.0.1 --port=5000
from flask import Flask,render_template,jsonify,request,url_for
import requests
import json
app = Flask(__name__, template_folder='./templates')

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
