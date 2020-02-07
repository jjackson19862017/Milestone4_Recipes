import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook' # Insert Database Name
app.config["MONGO_URI"] = os.getenv("MONGODB_URI") # Insert Database URI from MongoDB
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", page_title="REFRESHING EDIBLE CUISINE IN PORTABLE EXTERNAL SUPPORT")

@app.route('/view_recipes')
def view_recipes():
    recipes=mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes, page_title="RECIPE COLLECTION")

@app.route('/add_recipe')
def add_recipe():
    the_difficulty = mongo.db.difficulty.find()
    the_meal_type = mongo.db.mealtype.find()
    the_healthy = mongo.db.healthy.find()
    return render_template("addrecipe.html", difficulty = the_difficulty, mealtype = the_meal_type,healthy=the_healthy,  page_title="ADD RECIPE")

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('view_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    the_difficulty = mongo.db.difficulty.find()
    the_meal_type = mongo.db.mealtype.find()
    the_healthy = mongo.db.healthy.find()
    return render_template('editrecipe.html', recipe=the_recipe, difficulty = the_difficulty, mealtype = the_meal_type, healthy=the_healthy,page_title="EDIT RECIPE")

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'author':request.form.get('author'),
        'meal_type': request.form.get('meal_type'),
        'difficulty': request.form.get('difficulty'),
        'healthy':request.form.get('healthy'),
        'prep_time':request.form.get('prep_time'),
        'cooking_time':request.form.get('cooking_time'),
        'serves':request.form.get('serves'),
        'description':request.form.get('description'),
        'notes':request.form.get('notes'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('method'),
        'email':request.form.get('email')

    })
    return redirect(url_for('view_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('view_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)