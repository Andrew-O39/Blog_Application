import json
from typing import List, Dict

POSTS_FILE = 'posts.json'

def load_posts() -> List[Dict]:
    with open(POSTS_FILE, 'r') as file:
        return json.load(file)

def save_posts(posts: List[Dict]):
    with open(POSTS_FILE, 'w') as file:
        json.dump(posts, file, indent=4)