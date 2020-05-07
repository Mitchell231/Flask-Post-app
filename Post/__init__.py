from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


ENV = 'dev'

if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Felicity231@localhost/lexus'
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7df2da7a4b7c3696c1d0de09d273e0a8'

db = SQLAlchemy(app)


from Post import view # This is from view.py