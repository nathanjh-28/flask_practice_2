from flask_practice_app import app, db, bcrypt
from flask_practice_app.models import User, Post
from flask_practice_app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_u = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_u)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u and bcrypt.check_password_hash(u.password, form.password.data):
            login_user(u, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html')