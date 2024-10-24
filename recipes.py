from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)

    def __init__(self, title, ingredients, instructions, description=None, image_url=None):
        self.title = title
        self.ingredients = ', '.join(ingredients)
        return f"Recipe: {self.title}\nIngredients: {self.ingredients}\nInstructions: {self.instructions}\nDescription: {self.description}\nImage URL: {self.image_url}"
