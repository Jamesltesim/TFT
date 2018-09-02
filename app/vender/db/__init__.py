from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def query():


    pass

def insert(model):
    db.session.add(model)
    db.session.commit()
    pass

def update():
    pass

def delete():
    pass