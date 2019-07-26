from flask import Flask, render_template, flash, redirect, url_for, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from flaskforms import LoginForm, postform
from flask_login import LoginManager
login = LoginManager(app)
from models import Posts
from flask_login import current_user, login_user, logout_user

@app.route("/")
def root():
    return render_template("root.html")

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/woodlandm")
def woodlandm():
    return render_template("woodlandm.html")   

@app.route('/woodlandm/exampleclass1')
def woodlandmexampleclass1():
    return render_template('woodlandmexampleclass1.html')
@app.route('/woodlandm/exampleclass1P')
def woodlandmexampleclass1P():
    return redirect(url_for('woodlandmexampleclass1'))
if __name__ == "__main__":
    app.run(debug=True)