from main.models import User, Post
from main.forms import PostForm
from main import app,db
from flask import render_template,jsonify,request,url_for

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

@app.route("/", methods=['GET', 'POST'])
def home():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=1)
        db.session.add(post)
        db.session.commit()
    return render_template('home.html',posts=posts,form=form, legend='New Post')

@app.route("/topic")
def topic():
    return render_template('topic.html',title_var='Topic#1')
