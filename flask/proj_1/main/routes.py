from main.models import User, Post, Playlist, Song, load_user
from main.forms import PostForm
from main import app,db
from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_user, current_user, logout_user

import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = '83a29879ab1b4e76acb763bb3f2d8bcc'
SPOTIPY_CLIENT_SECRET = '1cc669adfa30443dbcf25eb52e43dbda'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:80/auth/'

class SpotifyApi():

    def __init__(self):
        self.SCOPE = 'user-read-private user-read-email user-library-read user-top-read playlist-read-private playlist-read-collaborative'
        self.CACHE = '.spotipyoauthcache'
        self.active=None
        self.playlists=None
        self.songs=None
        self.current_auth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=self.SCOPE,cache_path=self.CACHE )
    
    @staticmethod
    def activate(self,access_token):
        self.active = spotipy.Spotify(access_token)

    @staticmethod
    def call_playlists(self, current=0, next=5):
       self.playlists=self.active.current_user_playlists(limit=next, offset=current)#limit max 50 need to offset after 50 for next 50

    @staticmethod
    def call_songs(self, user_id, playlist_id, current=0, next=5):
        self.songs=self.active.user_playlist_tracks(user_id, playlist_id=playlist_id, fields=None, limit=next, offset=current, market=None)#limit max 100 need to offset after 100 for next 100


    @staticmethod
    def update_playlists(self,user_id):
        for playlist in range(0,len(self.playlists['items'])):
            try:
                playlist_db=Playlist(id=self.playlists['items'][playlist]['id'], title=self.playlists['items'][playlist]['name'],user_id=user_id)
                db.session.add(playlist_db)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

    @staticmethod
    def update_songs(self, user_id, playlist_id):
        for song in range(0,len(self.songs['items'])):
            song_db=Song(id=self.songs['items'][song]['track']['name'], name=self.songs['items'][song]['track']['name'], album=self.songs['items'][song]['track']['name'],playlist_id=playlist_id)
            try:    
                db.session.add(song_db)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

    @property
    def user_playlists(self):
        playlists=self.active.current_user_playlists(limit=1, offset=0)#limit max 50 need to offset after 50 for next 50
        for playlist in range(0,len(playlists['items'])):
            print(f"Playlist {playlist}: {playlists['items'][playlist]['name']}")
            print(f"Playlist ID {playlist}: {playlists['items'][playlist]['id']}")
        print(f"All total: {playlists['total']}")

spotify=SpotifyApi()

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<string:playlist_id>', methods = ['GET', 'POST'])
def Topic(playlist_id=None):
    if current_user.is_authenticated:
        print("Authenticated user")
        try:
            spotify.activate(spotify,current_user.access_token)
            me = spotify.active.me()#without this logout is not working properly. (verification for api access needed here)
        except Exception as e:
            print(e)
            logout_user()

        try:
            spotify.call_playlists(spotify, current=0, next=50)
            #spotify.update_playlists(spotify,me['id'])
            pass
        except Exception as e:
            print(e)
            pass
    else:
        print("Non-authenticated user")
    playlists = Playlist.query.all()
    if playlist_id==None:
        #playlist_selected = Playlist.query.get(1)
        playlist_selected = Playlist.query.first()
    else:
        spotify.call_songs(spotify,me['id'],playlist_id, current=0, next=50)
        #spotify.update_songs(spotify,me['id'],playlist_id)
        playlist_selected=Playlist.query.get_or_404(playlist_id)
    posts = playlist_selected.posts
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, user_id = 1, playlist_id = playlist_selected.id )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('Topic', playlist_id=playlist_selected.id))
    return render_template('home.html',posts = posts,form=form, playlists = playlists,playlist_selected = playlist_selected, spotify=spotify, legend = 'New Post')

@app.route('/login')
def Login():
    try:
        me = spotify.active.me()
        user=load_user(me['id'])
        spotify.activate(spotify,user.access_token)
        login_user(user, remember=True)
        return redirect(url_for('Topic'))
    except:
        return redirect(spotify.current_auth.get_authorize_url())

@app.route('/auth/',methods=['GET'])
def Auth():
    if request.method == 'GET':
        try:
            code = str(request.args['code'])
            token_info = spotify.current_auth.get_access_token(code)
            access_token = token_info['access_token']
            
        except Exception as e:
            print("Can not retrieve token")
            print(e)
            #me = spotify.active.me()
            #print(me)
            return redirect(url_for('Topic'))
        if access_token:
            try:
                spotify.activate(spotify,access_token)
                print(request.args.get('next'))
            except:
                print("Authentication failed")
                return redirect(url_for('Topic'))
            me = spotify.active.me()
            try:
                user=User(id=me['id'], username=me['display_name'],email=me['email'],image_url=me['images'][0]['url'],access_token=access_token)
                try:
                    user_from_db=load_user(me['id'])
                    user_from_db.access_token=access_token
                    db.session.commit()
                except Exception as e:
                    db.session.add(user)
                    db.session.commit()
                    print(e)
                    
                login_user(user, remember=True)
            except:
                user=load_user(me['id'])
                login_user(user, remember=True)
        next_page = request.args.get('next')
        return redirect('next_page') if next_page else redirect(url_for('Topic'))

    return redirect(url_for('Topic'))

