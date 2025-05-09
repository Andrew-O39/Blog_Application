import json
from typing import List, Dict

POSTS_FILE = 'posts.json'

def load_posts() -> List[Dict]:
    with open(POSTS_FILE, 'r') as file:
        return json.load(file)

def save_posts(posts: List[Dict]):
    with open(POSTS_FILE, 'w') as file:
        json.dump(posts, file, indent=4)


def add_post(author: str, title: str, content: str):
    posts = load_posts()
    new_id = max([post['id'] for post in posts], default=0) + 1
    posts.append({'id': new_id, 'author': author, 'title': title, 'content': content})
    save_posts(posts)

def delete_post(post_id: int):
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)

def update_post(post_id: int, author: str, title: str, content: str):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post.update({'author': author, 'title': title, 'content': content})
            break
    save_posts(posts)


def fetch_post_by_id(post_id):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

def update_post(post_id, author, title, content):
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post['author'] = author
            post['title'] = title
            post['content'] = content
            break
    save_posts(posts)