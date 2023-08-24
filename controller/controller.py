import json
from models.models import db,UserTable 
from flask import jsonify,render_template


def index():
    return render_template("index.html")


def create():
    db.create_all()
    db.session.commit()
    return "<h1>Hello create</h1"
    
    


# insert data into table.
def insert():
     data=UserTable(id=1,username="Prasanna",password="Hello")
     db.session.add(data)
     db.session.commit()
     return "<h1>Hello innsert</h1"

def list():
    data=UserTable.query.all()
   
    return render_template("index.html",data=data)

    
    