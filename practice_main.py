from flask import Flask, render_template

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

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)