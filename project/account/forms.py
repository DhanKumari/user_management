from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from project.models import User



class RegistrationForm(FlaskForm):
    first_name= StringField('Firstname', validators=[DataRequired()])
    last_name= StringField('lastname', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('username', validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    # def check_email(self, email):
    #     user= User.query.filter_by(email=email.data).first()
    #     if user:    
    #         raise ValidationError('your email has been registered alredy!')
        
    # def check_username(self, username):
    #     user= User.query.filter_by(username=username.data).first()
    #     if user:  
    #         raise ValidationError('username  is already present')






class LoginForm(FlaskForm):
    username=StringField('username', validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('login')




