from main.models import User, Post, Playlist
from main.forms import PostForm
from main import app,db
from flask import render_template,jsonify,request,url_for,redirect

import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = '83a29879ab1b4e76acb763bb3f2d8bcc'
SPOTIPY_CLIENT_SECRET = '1cc669adfa30443dbcf25eb52e43dbda'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:80/auth/'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<int:playlist_id>', methods = ['GET', 'POST'])
def Topic(playlist_id=None):
    playlists = Playlist.query.all()
    if playlist_id==None:
        playlist_selected = Playlist.query.get(1)
    else:
        playlist_selected=Playlist.query.get_or_404(playlist_id)
    posts = playlist_selected.posts
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, user_id = 1, playlist_id = playlist_selected.id )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('Topic', playlist_id=playlist_selected.id))
    return render_template('home.html',posts = posts,form=form, playlists = playlists,playlist_selected = playlist_selected, legend = 'New Post')

@app.route('/login')
def Login():
    return redirect(sp_oauth.get_authorize_url())

@app.route('/auth/',methods=['GET'])
def Auth():
    if request.method == 'GET':
        print('user_token')
        print(str(request.args['code']))
        code = str(request.args['code'])
        token_info = sp_oauth.get_access_token(code)
        access_token = token_info['access_token']
        if access_token:
            print("Access token available! Trying to get user information...")
            sp = spotipy.Spotify(access_token)
            results = sp.current_user()
            print(results)

    return redirect(url_for('Topic'))

