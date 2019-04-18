from main.models import User, Post, Playlist, Song, load_user
from main.forms import PostForm
from main import app,db
from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_user, current_user

import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = '83a29879ab1b4e76acb763bb3f2d8bcc'
SPOTIPY_CLIENT_SECRET = '1cc669adfa30443dbcf25eb52e43dbda'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:80/auth/'

class SpotifyApi():
    SCOPE = 'user-read-private user-read-email'
    CACHE = '.spotipyoauthcache'
    def __init__(self):
        self.active=None
        self.current_auth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=self.SCOPE,cache_path=self.CACHE )


spotify=SpotifyApi()

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<int:playlist_id>', methods = ['GET', 'POST'])
def Topic(playlist_id=None):
    if current_user.is_authenticated:
        print("Authenticated user")
    else:
        print("Non-authenticated user")
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
    return redirect(spotify.current_auth.get_authorize_url())

@app.route('/auth/',methods=['GET'])
def Auth():
    
    if request.method == 'GET':
        try:
            code = str(request.args['code'])
            token_info = spotify.current_auth.get_access_token(code)
            access_token = token_info['access_token']
        except:
            print("Can not retrieve token")
            return redirect(url_for('Topic'))
        if access_token:
            try:
                spotify.active = spotipy.Spotify(access_token)
            except:
                print("Authentication failed")
                return redirect(url_for('Topic'))
            results = spotify.active.me()
            try:
                user=User(id=results['id'], username=results['display_name'],email=results['email'],image_url=results['images'][0]['url'])
                try:
                    db.session.add(user)
                    db.session.commit()
                except:
                    db.session.rollback()
                login_user(user, remember=True)
            except:
                user=load_user(results['id'])
                login_user(user, remember=True)

    return redirect(url_for('Topic'))

