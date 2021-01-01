from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FormField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_practice_app.models import User
from flask_login import current_user
from wtforms.fields.html5 import URLField, TelField
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

#____________________________________________________________

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post It!')

#____________________________________________________________

class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code')
    area_code    = IntegerField('Area Code/Exchange')
    number       = StringField('Number')

#____________________________________________________________
class ContactForm(FlaskForm):
    #name
    name = StringField('Name', validators=[DataRequired()])
    #email
    email = StringField('Email',validators=[DataRequired(),Email()])
    #phone
    phone = IntegerField('Phone',validators=[NumberRange(min=100000000,max=99999999,message='Please enter a valid US Phone Number')])
    #subject
    subject = StringField('Message Subject', validators=[DataRequired()])
    #body
    body = TextAreaField('Message Body', validators=[DataRequired()])
    #join email list
    join = BooleanField('Join our Emailing List')
    #submit
    submit = SubmitField('Submit!')

#____________________________________________________________
class ChannelForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    notes = TextAreaField('Message Body', validators=[Length(max=280)])
    submit = SubmitField('Add Comment')

class ReplyForm(FlaskForm):
    reply = TextAreaField('Message Body', validators=[Length(min=1,max=140)])
    submit = SubmitField('Add Reply')
