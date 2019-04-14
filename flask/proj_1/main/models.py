'''
from main import db
db.create_all()
from main.models import User,Post,Playlist
user_1=User(username='Deniz',email='anadnas@demo.com',password='test')
playlist_1=Playlist(title='Playlist 1',json_content='song 1',user_id=user.id)
post_1=Post(title='Post 1',content='comment 1',user_id=user.id, playlist_id=playlist.id)
db.session.add(user_1)
db.session.add(playlist_1)
db.session.commit()
User.query.all()
User.query.first()
User.query.get(1)
user=User.query.filter_by(username='Deniz').first()
for post in user.posts:
    	print(post.title)
db.drop_all()
'''


from main import db
from datetime import datetime

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(60), nullable=False)
        playlist = db.relationship('Playlist', backref='author', lazy=True)
        posts = db.relationship('Post', backref='author', lazy=True)
        

        def __repr__(self):
            return f"User('{self.username}', '{self.email}')"




class Playlist(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        json_content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        posts = db.relationship('Post', backref='topic', lazy=True)

        def __repr__(self):
            return f"Playlist('{self.title}', '{self.date_posted}', '{self.json_content}')"

class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

        def __repr__(self):
            return f"Post('{self.title}', '{self.date_posted}')"
