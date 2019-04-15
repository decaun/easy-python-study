from main.models import User, Post, Playlist
from main.forms import PostForm
from main import app,db
from flask import render_template,jsonify,request,url_for,redirect


@app.route("/", methods=['GET', 'POST'])
@app.route("/<int:playlist_id>", methods=['GET', 'POST'])
def Topic(playlist_id=None):
    playlists = Playlist.query.all()
    if playlist_id==None:
        playlist_selected=Playlist.query.get(1)
    else:
        playlist_selected=Playlist.query.get_or_404(playlist_id)
    posts = playlist_selected.posts
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=1, playlist_id=playlist_selected.id )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('Topic', playlist_id=playlist_selected.id))
    return render_template('home.html',posts=posts,form=form, playlists=playlists,playlist_selected=playlist_selected, legend='New Post')

@app.route("/topic")
def topic():
    return render_template('topic.html',title_var='Topic#1')
