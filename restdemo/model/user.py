from restdemo.app import db


class User(db.model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))
