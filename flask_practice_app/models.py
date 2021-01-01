from datetime import datetime
from flask_practice_app import app, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #relationships
    posts = db.relationship('Post', backref='author', lazy=True)
    channels = db.relationship('Channel', backref='channel_author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#____________________________________________________________
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

#____________________________________________________________
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, 
        default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer)
    subject = db.Column(db.String(75), nullable=False)
    body = db.Column(db.String(280), nullable=False)
    join = db.Column(db.Boolean)
    #relationship
    channels = db.relationship('Channel',backref='thread',lazy=True)

#____________________________________________________________
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)
    date_posted = db.Column(
        db.DateTime, 
        nullable=False, 
        default=datetime.utcnow)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id'), 
        nullable=False)
    contact_id = db.Column(
        db.Integer,
        db.ForeignKey('contact.id'),
        nullable=False)

# class Reply(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_posted = db.Column(
#         db.DateTime, 
#         nullable=False, 
#         default=datetime.utcnow)
    
#     user_id = db.Column(
#         db.Integer, 
#         db.ForeignKey('user.id'), 
#         nullable=False)