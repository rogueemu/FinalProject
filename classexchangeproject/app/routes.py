from flask import Flask, render_template, flash, redirect
from config import Config
from app import app
from flaskforms import postform, LoginForm

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

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
            'author': {'username': 'user1'},
            'body': 'Body1'
        },
        {
            'author': {'username': 'user2'},
            'body': 'body2'
        }
    ]
    return render_template('woodlandmexampleclass1.html', form=form, user=user, posts=posts)    