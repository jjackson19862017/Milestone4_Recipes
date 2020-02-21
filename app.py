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

""" Welcome Page """
@app.route('/')
def view_recipes():
    """ Sorts by Meal_type in ascending order """
    recipes=mongo.db.recipes.find().sort([('views', -1)])
    

    """ Adding Functionality to Search Dropdown Menu """
    listDiff = list(mongo.db.difficulty.find())
    return render_template("index.html", recipes=recipes, listDifficulty = listDiff, page_title="RECIPE COLLECTION")

""" Page that allows you to add Recipes """
@app.route('/add_recipe')
def add_recipe():
    """ Gets all my collections ready for putting into Drop Menus """
    the_difficulty = mongo.db.difficulty.find()
    the_meal_type = mongo.db.mealtype.find()
    the_healthy = mongo.db.healthy.find()
    return render_template("addrecipe.html", difficulty = the_difficulty, mealtype = the_meal_type, healthy=the_healthy,  page_title="ADD RECIPE")

""" Sends the New Recipe to Mongo """
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ Inserts all fields into a record """
    recipes=mongo.db.recipes
    recipes.insert_one({

        'recipe_name':request.form.get('recipe_name'),
        'author':request.form.get('author'),
        'recipe_image':request.form.get('recipe_image'),
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
        'email':request.form.get('email'),
        'views':0
    })

    return redirect(url_for('view_recipes'))

""" Page that allows you to edit Recipes """
@app.route('/edit_recipe/<recipe_id>', methods=['GET','POST'])
def edit_recipe(recipe_id):
    """ Gets the correct recipe using the find_one function and the recipe_id """
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    """ Gets all my collections ready for putting into Drop Menus """
    the_difficulty = mongo.db.difficulty.find()
    the_meal_type = mongo.db.mealtype.find()
    the_healthy = mongo.db.healthy.find()
    return render_template('editrecipe.html', recipe=the_recipe, difficulty = the_difficulty, mealtype = the_meal_type, healthy=the_healthy, page_title="EDIT RECIPE")
    
""" Function that updates a recipe after being edited """
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """ Updates all fields into a record """
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'author':request.form.get('author'),
        'recipe_image':request.form.get('recipe_image'),
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
        'email':request.form.get('email'),
        'views':request.form.get('views')

    })
    return redirect(url_for('view_recipes'))


""" Page that deletes recipes """
@app.route('/delete_recipe/<recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('view_recipes'))

""" Page that allows you to see the Recipe in Detail """
@app.route('/view_recipe_details/<recipe_id>')
def view_recipe_details(recipe_id):
    recipes = mongo.db.recipes
    recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('detailsrecipe.html', recipe=the_recipe,page_title="RECIPE DETAILS")

"""Search Mongo for Recipes"""
@app.route('/find_recipes', methods=['GET', 'POST'])
def find_recipes():
    if request.method=='POST':        
        # get the search term
        search_field = request.form.get("search_field")
        #  create the index
        mongo.db.recipes.create_index( [("$**", 'text')] )
         # search with the search term that came through the form
        cursor = mongo.db.recipes.find({ "$text": { "$search": search_field } })
        recipes_count = cursor.count()
        recipes = [recipe for recipe in cursor]
        # send recipes to page
        return render_template('searchrecipes.html', recipes=recipes, query=search_field, rec_count=recipes_count)
    return render_template('searchrecipes.html')

"""Search Mongo for Users Email"""
@app.route('/find_user', methods=['GET', 'POST'])
def find_user():
    if request.method=='POST':        
        # get the search term
        user_field = request.form.get("user_field")
        #  create the index
        # search with the search term that came through the form
        cursor = mongo.db.recipes.find({ "email": user_field })
        recipes = [recipe for recipe in cursor]
        # send recipes to page
        return render_template('userrecipes.html', recipes=recipes, query=user_field)
    return render_template('userrecipes.html')

""" Quick Search Feature - Not Finished """
"""
@app.route('/find_recipes')
def search_recipes():
    mycol=mongo.db.recipes
    myquery={'difficulty':'Easy'}
    query = mycol.find(myquery)
    recipes = [recipe for recipe in myquery]
    return render_template('searchrecipes.html',recipes=recipes, query="Easy")
"""

""" Products Page """
@app.route('/view_products')
def view_products():
    """ Sorts by Product Name in ascending order """
    products=mongo.db.products.find().sort('product_name', 1)

    return render_template("products.html", products=products, page_title="OUR PRODUCTS")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)