#views

from flask import Blueprint,flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user , current_user
from project.models import User
from project import db
from project.account.forms import RegistrationForm,LoginForm



authB = Blueprint('auth',__name__)

@authB.route('/welcome',methods=['GET','POST'])
def welcome():
    return render_template('welcome.html',name=current_user)

@authB.route('/')
def firstpage():
    return render_template('firstpage.html')


#register
@authB.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user=User(first_name=form.first_name.data,
                last_name=form.last_name.data,
                email =form.email.data,
                username=form.username.data,
                password=form.password.data
                  )
        useremail=User.query.filter_by(email=form.email.data).first()
        username=User.query.filter_by(username=form.username.data).first()
        if username:
            flash('username already present ')
            return render_template('register.html',form=form)
        elif useremail:
            flash('email already present ')
            return render_template('register.html',form=form)
        db.session.add(user)
        db.session.commit()
        flash('thanks for registration')
        return redirect(url_for('auth.login'))
    return render_template('register.html',form=form)
        # if not useremail and not username:
        #     db.session.add(user)
        #     db.session.commit()
        #     flash('thanks for registration')
        #     return redirect(url_for('auth.login'))
        # else:
        #     flash('email or username already present')
            #return "email or username alredy present "
    #return render_template('register.html',form=form)

#login
@authB.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(username= form.username.data).first()
        if not user:
            flash ("user not present ")
            return render_template('login.html',form=form)

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('log in success!')
            return redirect(url_for('auth.welcome'))
        else:
            flash('incorrect password or username ')
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)



#logout
@authB.route('/logout', methods=['GET','POST'])
def logout():   
    logout_user()
    return redirect(url_for("auth.firstpage"))
