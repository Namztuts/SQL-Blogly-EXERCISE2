#python3 -m unittest test.py | run test

from unittest import TestCase
from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///post_db_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class PostViewsTestCase(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample user and post before each test"""
        db.session.remove()

        user = User(first_name="TestFirst", last_name="TestLast", img_url='www.google.com')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.user = user
        

        post = Post(title="TestTitle", content="TestContent", user_id=f"{user.id}" )
        db.session.add(post)
        db.session.commit()

        self.post_id = post.id
        self.title = post.title
        self.content = post.content
        self.post = post

    def tearDown(self):
        """Clean up any messed up test after each test"""

        db.session.rollback()

    def test_list_posts(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestTitle', html)

    def test_show_post(self):
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>TestTitle</h1>', html) 
            
    def test_add_post(self):
        with app.test_client() as client:
            data = {"post_title": "TestTitle2", "post_content": "TestContent2"}
            resp = client.post(f"/users/{self.user_id}/posts/new", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<p>{self.post.content}', html)
            
    def test_edit_post(self):
        with app.test_client() as client:
            data = {"post_title": "TestTitle2", "post_content": "TestContent2"}
            resp = client.get(f"/posts/{self.post.id}/edit", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'value="{self.post.content}"', html)