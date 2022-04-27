from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'Title': 'First blog post',
        'Author': 'Abhijeet Prajapati',
        'date': 'April 26, 2022',
        'content': '1st blog post by me'
    },
    {
        'Title': 'Second blog post',
        'Author': 'Abhijeet Prajapati',
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