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
    return render_template("addrecipe.html", page_title="ADD RECIPE")




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)