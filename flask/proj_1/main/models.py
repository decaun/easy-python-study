'''
from main import db
db.create_all()
from main.models import User,Post,Playlist,Song


user_1=User(username='Deniz',email='anadndas@demo.com',image_url='test')
db.session.add(user_1)
db.session.commit()
user=User.query.get(1)

playlist_1=Playlist(title='Playlist 1',user_id=user.id)
db.session.add(playlist_1)
db.session.commit()
playlist=Playlist.query.get(1)

song_1=Song(name='Song 1',album='album 1',playlist_id=playlist.id)
db.session.add(song_1)
db.session.commit()
song=Song.query.get(1)

song_2=Song(name='Song 2',album='album 1',playlist_id=playlist.id)
db.session.add(song_2)
db.session.commit()
song2=Song.query.get(2)

post_1=Post(title='Post 1',content='comment 1',user_id=user.id ,playlist_id=playlist.id ,song_id=song.id)
db.session.add(post_1)
db.session.commit()
post=Post.query.get(1)

post_2=Post(title='Post 1',content='comment 1',user_id=user.id ,playlist_id=playlist.id )
db.session.add(post_1)
db.session.commit()
post2=Post.query.get(1)

User.query.all()
User.query.first()
User.query.get(1)
user=User.query.filter_by(username='Deniz').first()
for post in user.posts:
    	print(post.title)
db.drop_all()

user=User.query.get(1)
user.playlist
user.comment

playlist=Playlist.query.get(1)
playlist.posts
playlist.author

post=Post.query.get(1)
post.author
post.topic

pip install flask-dance[sqla]
'''


from main import db,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(30), unique=True, nullable=False)
        image_url = db.Column(db.String(120), nullable=False)
        playlist = db.relationship('Playlist', backref='author', lazy=True)
        posts = db.relationship('Post', backref='author', lazy=True)
        

        def __repr__(self):
            return f"User('{self.id}', {self.username}', '{self.email}')"



class Playlist(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        posts = db.relationship('Post', backref='topic', lazy=True)
        songs = db.relationship('Song', backref='topic', lazy=True)

        def __repr__(self):
            return f"Playlist('{self.title}', '{self.date_posted}')"


class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=True)
        playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

        def __repr__(self):
            return f"Post('{self.title}', '{self.date_posted}')"

class Song(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        album = db.Column(db.String(100), nullable=False)
        posts = db.relationship('Post', backref='song', lazy=True)
        playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

        def __repr__(self):
            return f"Song('{self.name}', '{self.album}')"
        