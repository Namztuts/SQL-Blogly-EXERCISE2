"""Seed file to make sample data for users db."""
   #run this file in ipython3 | %run seed.py
from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it | deletes all
User.query.delete()

# Add users
johnB = User(first_name='John', last_name='Bush', img_url='https://static.wixstatic.com/media/4c37a2_e5a09e4a8a1749ad9812a980042220df~mv2.jpg/v1/fill/w_920,h_554,al_c,q_85/JohnBush.jpg')
jeffC = User(first_name='Jeff', last_name='Collins', img_url='https://variety.com/wp-content/uploads/2024/05/Jeff-Collins-Headshot_Credit-Holly-Lynch-e1715988143879.jpg?w=1000&h=667&crop=1')
amyP = User(first_name='Amy', last_name='Phillips', img_url='https://thecomicscomic.com/wp-content/uploads/2018/11/amyphillips.png')

# Add posts
john_post = Post(title='First post!', content='How do you like it here?', user_id=1)
john_post2 = Post(title='Second post...', content='Im getting used to this.', user_id=1)
jeff_post = Post(title='First post!', content='Does anybody know this John guy?', user_id=2)
jeff_post2 = Post(title='Second post...', content='John wont stop making innapropriate jokes.', user_id=2)
amy_post = Post(title='First post!', content='We need more woman on this site!', user_id=3)
amy_post2 = Post(title='Second post...', content='#feelingalone', user_id=3)
#john_post.users.first_name | returns 'John'!!!!!

# Add new objects to session, so they'll persist
db.session.add_all([johnB, jeffC, amyP])
db.session.add_all([john_post, john_post2, jeff_post, jeff_post2, amy_post, amy_post2])

# Commit--otherwise, this never gets saved!
db.session.commit()


#get a user by id      | user1 = User.query.get(1)
#access date from user | user1.first_name
#access post data      | user1.posts
#itterate through posts with a loop | for post in posts: print(post.title)
