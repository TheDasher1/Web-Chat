from turtle import title
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f0db6bf5254931c37d94eb60cf9bf80d611c9ca9f425ca506ea6d95da45f211b'

posts = [
    {
        'title': 'First blog post',
        'author': 'Abhijeet Prajapati',
        'date': 'April 26, 2022',
        'content': '1st blog post by me'
    },
    {
        'title': 'Second blog post',
        'author': 'Abhijeet Prajapati',
        'date': 'April 27, 2022',
        'content': '2nd blog post by me'
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', title='My Flask Blog', postsArgs=posts)

@app.route('/register')
def register():
    form = RegistrationForm()

    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
    return render_template("about.html", title='About us page')