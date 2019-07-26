from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\users\andre\woodlandmexample1.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = FALSE
db = SQLAlchemy(app)

class woodlandmexampleclass1(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    message = db.Column(db.String)