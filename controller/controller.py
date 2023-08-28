import json
from models.models import db,User 
from flask import jsonify,render_template,request,redirect,flash,url_for,session,Blueprint
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session


controllers = Blueprint('controllers', __name__)


import time
def index():
    return render_template("index.html")


def create():
    db.create_all()
    db.session.commit()
    return "<h1>Hello create</h1"
    
    


#insert data into table.
def insert():
     data=User(user_id=1,username="Prasanna",password="Hello",email="happyprasan@gmail.com")
     db.session.add(data)
     db.session.commit()
     return "<h1>Hello innsert</h1"

def list():
    data=User.query.all()
   
    return render_template("index.html",data=data)


#AUTHENTICATION.

def login_signup():
    return render_template('authentication.html')

def signup():
    if request.method=='POST':
        email=request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("password")
        password_confirm=request.form.get("password_confirm")

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose another.', 'danger')
            return "<h1>Vak</h1>"
        elif password != password_confirm:
            flash("Not",'danger')
            return  redirect(url_for('login_signup'))
        else:
            session['username']=username
            password_hash = generate_password_hash(password)
            user=User(username=username,password_hash=password_hash,email=email)
            db.session.add(user)
            db.session.commit()
            
            flash("added",'danger')
            
            
            return  redirect('/')
        



def login():
    username=request.form.get("username")
    password=request.form.get("password")
    user=User.query.filter_by(username=username).first()
  

    if user:
         
        
        if  check_password_hash(user.password_hash, password):
             session['username']=username
             login_user(user)
             
            
             return redirect(url_for('blueprint.index')) 
        return "<h1>Incorrect Password</h1>"
    
    return "<h1>No user exist</h1>"

   

def logout():
    # logout_user()
    session.pop('username',None)
    return redirect(url_for('blueprint.index'))


def error():
    return "<h1>ERRO</h1>"

@controllers.route('/dashboard')
@login_required
def dashboard():
    var=session["username"]
    user=User.query.filter_by(username=var).first()
    return render_template("dashboard.html",user=user)


def create_blog():
    if   session.get("username")  is not None:
      return render_template("editor.html")
    else:
        return redirect(url_for('blueprint.login_signup'))

    
    