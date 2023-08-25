from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    posts = db.relationship('BlogPost', backref='author', lazy=True)  # One-to-many relationship
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<userid %r>' % self.id
    
class BlogPost(db.Model):
    post_id=db.Column(db.Integer,primary_key=True)
    user=db.relationship('User',backref='person',lazy=True)
    content=db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

