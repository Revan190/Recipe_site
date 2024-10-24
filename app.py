from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
import os
import json
from recipes import Recipe
from utils.helpers import load_user, User

app = Flask(__name__)

app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

IMAGE_FOLDER = 'static/images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

RECIPES_FILE = 'data/recipes.json'

def load_recipes(filename=RECIPES_FILE):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_recipes(recipes, filename=RECIPES_FILE):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(recipes, file, ensure_ascii=False, indent=4)

recipes = load_recipes()

@login_manager.user_loader
def load_user(user_id):
    return load_user(user_id)
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        
        if not title or not ingredients or not instructions:
            return render_template('add_recipe.html', error="All fields are required.")
        
        image = request.files['image']
        if not image:
            return render_template('add_recipe.html', error="You need to upload an image.")

        image_filename = image.filename
        image.save(os.path.join(app.config['IMAGE_FOLDER'], image_filename))

        new_recipe = Recipe(title, ingredients, instructions, description, image_filename)
        recipes.append(new_recipe)

        save_recipes(recipes)
        return redirect(url_for('index'))

    return render_template('add_recipe.html')

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    if recipe_id < len(recipes):
        recipe = recipes[recipe_id]
        return render_template('recipe_detail.html', recipe=recipe, recipe_id=recipe_id)
    else:
        return "Recipe not found", 404

users_db = {
    'user1': {'password': generate_password_hash('your_password1')},
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and check_password_hash(user['password'], password):
        return User(username, username)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate(username, password)
        if user:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
