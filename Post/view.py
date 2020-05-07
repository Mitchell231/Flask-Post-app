from flask import render_template, url_for, redirect, request
from Post import app, db
from Post.db_models import Post



@app.route("/")
def index():
	posts = Post.query.all()
	return render_template('index.html', posts=posts)


@app.route("/post", methods=['GET', 'POST'])
def post():
	if request.method == 'POST':
		post = Post(title=request.form['title'], content=request.form['content'])
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('post.html', title='Post')



@app.route("/update/<int:post_id>", methods=['GET', 'POST'])
def update_post(post_id):
	return render_template('post.html', title='Update Post', post=post)


@app.route("/delete/<int:post_id>", methods=['POST'])
def delete_post(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('index'))

