import json
from models.models import db,User ,BlogPost
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
            return  redirect(url_for('blueprint.login_signup'))
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

@login_required
def create_blog():
    if   (session.get("username") ) is not None:
       if request.method =="POST":
           var=session["username"]
           user=User.query.filter_by(username=var).first()
           editor_content=request.form.get('editor_content')
           title=request.form.get('title')
           category=request.form.get('category')
           post=BlogPost(content=editor_content,user=user,user_id=user.get_id(),category=category,title=title)
           db.session.add(post)
           db.session.commit()
           
        
       return render_template("editor.html")
    else:
        return redirect(url_for('blueprint.login_signup'))
    

import re

def blogfeed():
    
    blogss=BlogPost.query.all()
    blogs = [re.sub(r'<.*?>', '', blog.content) for blog in blogss]
    return render_template("index.html",blogss=blogss,blogs=blogs,zip=zip)


def index():
    blogss=BlogPost.query.all()
    blogs = [re.sub(r'<.*?>', '', blog.content) for blog in blogss]
    return render_template("index.html",blogss=blogss,blogs=blogs,zip=zip)



from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
#api section



def  api_signup():
        data=request.get_json()
        email=data.get("email")
        username=data.get("username")
        password=data.get("password")
        password_confirm=data.get("password_confirm")

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"status":"Failed","Message":"User Already exist"}), 200
            
        elif password != password_confirm:
            return jsonify({"status":"Failed","Message":"Password and Confirm Password doesnt match"}), 200
        else:
            access_token = create_access_token(identity=username)
            password_hash = generate_password_hash(password)
            user=User(username=username,password_hash=password_hash,email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify({"status":"Success","Message":"User Registered Successfully","access_token":access_token}), 200
            
           
def login_api():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    user=User.query.filter_by(username=username).first()
  

    if user:    
        if  check_password_hash(user.password_hash, password):
             access_token = create_access_token(identity=username)
             return jsonify({"message": "User is verified successfully","access_token":access_token}), 201 
        return  jsonify({"message": "Incorrect Email or Password"}), 400
    
    return  jsonify({"message": "No user exists"}), 400
            
          
