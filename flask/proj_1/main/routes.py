from main.models import User, Post, Playlist, Song, load_user, PlaylistSchema
from main.forms import PostForm
from main import app,db,spotify
from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_user, current_user, logout_user
import spotipy


@app.route('/', methods = ['GET', 'POST'])
@app.route('/<int:playlist_id>', methods = ['GET', 'POST'])
@app.route('/<string:topic>/<int:playlist_id>', methods = ['GET', 'POST'])
def Topic(playlist_id=None,topic=None):
    if current_user.is_authenticated:
        print("Authenticated user")
        try:
            spotify.activate(current_user.access_token)
            me = spotify.active.me()#without this logout is not working properly. (verification for api access needed here)
        except Exception as e:
            print(e)
            logout_user()

        try:
            spotify.call_playlists(current=0, next=50)
            spotify.insert_playlists(me['id'])
        except Exception as e:
            #print(e)
            pass
    else:
        print("Non-authenticated user")
    playlists = Playlist.query.all()

    if playlist_id==None:
        #playlist_selected = Playlist.query.get(1)
        playlist_selected = Playlist.query.first()
    else:
        playlist_selected=Playlist.query.get(playlist_id)
        if current_user.is_authenticated:
            spotify.call_songs(me['id'],playlist_selected.spotify_id, current=0, next=50)
        #    print(spotify.songs)
            spotify.insert_songs(playlist_id)
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
        real_user=User.query.filter_by(spotify_id=me['id']).first()
        user=load_user(real_user.id)
        spotify.activate(user.access_token)
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
            me = spotify.active.me()
            spotify.__init__()
            return redirect(url_for('Topic'))
        if access_token:
            try:
                spotify.activate(access_token)
            except:
                print("Authentication failed")
                logout_user()
                return redirect(url_for('Topic'))
            me = spotify.active.me()
            try:
                real_user=User.query.filter_by(spotify_id=me['id']).first()
                real_user.access_token=access_token
                db.session.commit()
                login_user(real_user, remember=True)
            except Exception as e:
                user=User(spotify_id=me['id'], username=me['display_name'],email=me['email'],image_url=me['images'][0]['url'],access_token=access_token)
                db.session.rollback()
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
            
        #next_page = request.args.get('next')
        #return redirect('next_page') if next_page else redirect(url_for('Topic'))

    return redirect(url_for('Topic'))

@app.route('/getplaylist',methods=['GET'])
def Get_user_data():
    playlist_call = Playlist.query.with_entities(Playlist.id, Playlist.title, Playlist.genre).slice(int(request.headers['Counter']), 1+int(request.headers['Counter'])).all()
    playlist_schema = PlaylistSchema(many=True)
    output = playlist_schema.dump(playlist_call).data
   
    return jsonify(output)