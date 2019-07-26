from flask import Flask, render_template, flash, redirect
from config import Config
import flaskapp
from postform import postform

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("root.html")

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/woodlandm")
def woodlandm():
    return render_template("woodlandm.html")   

@app.route('/woodlandm/exampleclass1', methods=['GET', 'POST'])
def woodlandmexampleclass1():
    form = postform()
    if form.validate_on_submit():
        flash('Post requested for user {}'.format(
            form.username.data))
        return redirect('/woodlandm/exampleclass1')
    user = {"username": "ebic gamer"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('woodlandmexampleclass1.html', form=form, user=user, posts=posts)    