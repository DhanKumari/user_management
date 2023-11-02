# first file that runs , db , instance , login 
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_restful import  Api
db= SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY']='secretkey'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False    
db.init_app(app)


#login set up 
login_manager = LoginManager()
login_manager.login_view='account.views.login'
login_manager.init_app(app)

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






from .account.views import authB
app.register_blueprint(authB)


Migrate(app,db)