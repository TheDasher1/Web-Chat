from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route("/about")
def about():
    return render_template("about.html", title='About us page')