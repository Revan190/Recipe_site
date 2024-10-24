import json
from flask_login import UserMixin

def load_recipes(filename='data/recipes.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_recipes(recipes, filename='data/recipes.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(recipes, file, ensure_ascii=False, indent=4)

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

def load_user(user_id):
    users = {
        '1': User('1', 'user1'),
        '2': User('2', 'user2')
    }
    return users.get(user_id)
