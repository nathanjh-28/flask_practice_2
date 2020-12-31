from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

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

# secret key
app.config['SECRET_KEY'] = 'SAPNgFaCXp6CZTjq'

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)