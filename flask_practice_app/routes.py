from flask_practice_app import app, db
from flask_practice_app.models import User, Post
from flask_practice_app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect

# ===================================================================
#_________   Dummy Data
posts = [{
'author':'Nathan Harris',
'title':'Blog Post 1',
'content':'Lorem Ipsum blah blah blah',
'date_posted':'April 20, 2018'
},
{
'author':'Jeff Smitty',
'title':'Blog Post 2',
'content':'hello world my name is Jeffff and I like to party!',
'date_posted':'May 1, 2018'
}]
# ===================================================================

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)