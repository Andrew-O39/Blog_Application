from flask import Flask, render_template, request, redirect, url_for
from json_data import load_posts, add_post, save_posts, fetch_post_by_id, update_post

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        add_post(author, title, content)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()
    updated_posts = [post for post in posts if post['id'] != post_id]
    save_posts(updated_posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        update_post(post_id, author, title, content)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)