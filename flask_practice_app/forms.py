from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_practice_app.models import User
from flask_login import current_user
from wtforms.fields.html5 import URLField
# ===========================================================

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[ 
        DataRequired(), 
        Length(min=2,max=20 )])
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email()])
    
    password = PasswordField('Password', validators=
        [DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo( 'password' )])
    
    submit = SubmitField( 'Sign Up' )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.  Please choose a different one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.  Please choose a different one')

#____________________________________________________________

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email()])
    
    password = PasswordField('Password', validators=
        [DataRequired()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField( 'Login' )

#____________________________________________________________

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators=[
            DataRequired(), 
            Length(min=2, max=20)])

    email = StringField('Email', 
        validators=[
            DataRequired(), 
            Email()])

    picture = URLField('Update Profile Picture')

    submit = SubmitField('Update Account')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken.  Please choose a different one')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken.  Please choose a different one')