import json
import os
from typing import List, Dict

POSTS_FILE = 'posts.json'

def load_posts() -> List[Dict]:
    """Load all blog posts from the JSON file."""
    if not os.path.exists(POSTS_FILE):
        # If the file doesn't exist, return an empty list
        return []

    try:
        with open(POSTS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The posts file contains invalid JSON.")
        return []
    except Exception as e:
        print(f"Unexpected error reading posts file: {e}")
        return []

def save_posts(posts: List[Dict]):
    """Save all blog posts to the JSON file."""
    with open(POSTS_FILE, 'w') as file:
        json.dump(posts, file, indent=4)


def add_post(author: str, title: str, content: str):
    """Create a new post and save it to the JSON file."""
    posts = load_posts()

    # Generate a new unique ID by finding the max ID in existing posts
    new_id = max([post['id'] for post in posts], default=0) + 1

    # Create and append the new post and save it to the JSON file
    posts.append({'id': new_id, 'author': author, 'title': title, 'content': content})
    save_posts(posts)

def delete_post(post_id: int):
    """Delete a blog post with the given ID from the list and save the updated list."""
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)

def update_post(post_id: int, author: str, title: str, content: str):
    """Update an existing post with new data."""
    posts = load_posts()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        post.update({'author': author, 'title': title, 'content': content})
        save_posts(posts)


def fetch_post_by_id(post_id):
    """Return a single post by ID, or None if not found."""
    posts = load_posts()
    return next((post for post in posts if post['id'] == post_id), None)
