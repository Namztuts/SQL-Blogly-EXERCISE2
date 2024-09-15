"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy() 

def connect_db(app):
  db.app = app
  db.init_app(app)

DEFAULT_URL = 'https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png'

#user1 = User(first_name='Jacob',last_name='Man',img_url='www.google.com')
class User (db.Model):
  __tablename__ = 'users'
  
  @property #@property allows me to access this method with .full_name (as an attribute) instead of .full_name() (as a method call) 
  def full_name(self):
    '''States a user's full name'''
    return f'{self.first_name} {self.last_name}'
  
  id = db.Column(
    db.Integer, 
    primary_key=True, 
    autoincrement=True)
  
  first_name = db.Column(
    db.String(25),
    nullable=False)
  
  last_name = db.Column(
    db.String(25),
    nullable=False)
  
  img_url = db.Column(
    db.String(200),
    nullable=False,
    default=DEFAULT_URL)
  
class Post (db.Model):
  __tablename__ = 'posts'
  
  id = db.Column(
    db.Integer, 
    primary_key=True, 
    autoincrement=True)
  
  title = db.Column(
    db.Text,
    nullable=False)
  
  content = db.Column(
    db.Text,
    nullable=False)
  
  created_at = db.Column(
    db.DateTime, 
    default=func.now()) #date and time
  
  user_id = db.Column(
    db.Integer,
    db.ForeignKey('users.id'))
  
  users = db.relationship('User', backref ='posts')