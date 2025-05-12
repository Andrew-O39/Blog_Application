from flask import Flask, render_template, request, redirect, url_for
from json_data import load_posts, add_post,delete_post, fetch_post_by_id, update_post

app = Flask(__name__)


@app.route('/')
def index():
    """Display all blog posts on the homepage."""
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Display the add post form (GET) or handle form submission to add a new post (POST)."""
    if request.method == 'POST':
        # Get form data from the submitted POST request
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Call a helper function to create and save the new post
        add_post(author, title, content)
        return redirect(url_for('index'))

    # Redirect to the homepage after adding the post
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Securely delete a blog post via POST request."""
    delete_post(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Update an existing blog post."""
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Get updated data from form
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Save the updated post
        update_post(post_id, author, title, content)
        return redirect(url_for('index'))

    # Display update form pre-filled with post data
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)