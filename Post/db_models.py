from datetime import datetime
from Post import db, app


class Post(db.Model):
	__searchable__ = ['title', 'content']
	__tablename__ = 'post'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120))
	content = db.Column(db.Text())

	def __init__(self,   title, content):
		self.title = title
		self.content = content

	