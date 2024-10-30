# Recipe_site
 
Recipe_site/      # Main project directory
    Recipe_site/data/      # Directory containing data files
        Recipe_site/data/recipes.json      # JSON file containing recipe data
    Recipe_site/images/      # Directory for recipe images
        Recipe_site/images/recipe1.jpg      # Image file for recipe 1
        Recipe_site/images/recipe2.jpg      # Image file for recipe 2
    Recipe_site/static/      # Directory for static files (CSS, JS)
        Recipe_site/static/scripts/         # JavaScript files
            Recipe_site/static/scripts/main.js      # Main JavaScript file for client-side functionality
        Recipe_site/static/styles/          # CSS files
            Recipe_site/static/styles/styles.css      # Custom styles for the application
            Recipe_site/static/styles/tailwind.css      # Tailwind CSS framework file
    Recipe_site/templates/      # Directory for HTML templates
        Recipe_site/templates/components/      # Reusable HTML components
            Recipe_site/templates/components/recipe_card.html      # Template for displaying a recipe card
            Recipe_site/templates/components/search_bar.html       # Template for the search bar component
        Recipe_site/templates/layout/      # Layout templates
            Recipe_site/templates/layout/footer.html      # Footer layout template
            Recipe_site/templates/layout/header.html      # Header layout template
        Recipe_site/templates/add_recipes.html      # Template for adding new recipes
        Recipe_site/templates/base.html      # Base template for all pages
        Recipe_site/templates/index.html      # Homepage template
        Recipe_site/templates/recipe_detail.html      # Template for displaying detailed recipe information
    Recipe_site/utils/      # Directory for utility functions
        Recipe_site/utils/__init__.py      # Initialization file for the utils package
        Recipe_site/utils/helpers.py      # Helper functions for various tasks
    Recipe_site/__init__.py      # Initialization file for the main package
    Recipe_site/.gitattributes      # Git attributes file
    Recipe_site/.gitignore      # Git ignore file
    Recipe_site/app.py      # Main application file that runs the Flask server
    Recipe_site/recipes.py      # File containing functions for managing recipes
    Recipe_site/requirements.txt      # File listing the required Python packages for the project
    Recipe_site/tailwind.config.js      # Configuration file for Tailwind CSS

# How to Run

Install Dependencies:
Make sure you have Python and pip installed. Then, navigate to the project directory in your terminal and run:

```pip install -r requirements.txt```
Run the Application:
Launch the application by executing:

```python app.py```
The application will be accessible at http://localhost:5000.

# How to Use

**Homepage:**
When you open the application, you will see the homepage (index.html), which displays featured recipes and a search bar.

Searching for Recipes:
Use the search bar to find recipes by name or ingredient. The search results will be displayed using the recipe_card.html component.

Adding Recipes:
Navigate to the "Add Recipes" page (add_recipes.html) to submit new recipes. Fill out the required fields and upload images as needed.

Viewing Recipe Details:
Click on a recipe card to view more details about the recipe, which will be shown using the recipe_detail.html template.

Responsive Design:
The site utilizes Tailwind CSS for responsive design, ensuring a good user experience on various devices.

# Future Enhancements
Future updates may include:

User authentication for saving favorite recipes.
Integration with external recipe APIs for a broader selection of recipes.
Enhanced search functionality with filters (e.g., dietary restrictions, preparation time).
A mobile application version for easier access to recipes on the go.