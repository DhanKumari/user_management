from project import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model,UserMixin):

    __tablename__ ='users'

    id= db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, first_name,last_name, email,username,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f"{self.username}"