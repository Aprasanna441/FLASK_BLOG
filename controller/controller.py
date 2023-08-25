import json
from models.models import db,User 
from flask import jsonify,render_template,request


def index():
    return render_template("index.html")


def create():
    db.create_all()
    db.session.commit()
    return "<h1>Hello create</h1"
    
    


# insert data into table.
def insert():
     data=User(user_id=1,username="Prasanna",password="Hello",email="happyprasan@gmail.com")
     db.session.add(data)
     db.session.commit()
     return "<h1>Hello innsert</h1"

def list():
    data=User.query.all()
   
    return render_template("index.html",data=data)


#AUTHENTICATION.
def signup():
    return render_template('authentication.html')

def login():
    name=request.form.get("username")
    sport=request.form.get("password")
    return "<h1>Login success</h1>"

    
    