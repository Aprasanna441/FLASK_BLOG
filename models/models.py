from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class UserTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<userid %r>' % self.id
    
class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
