import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes' # Insert Database Name
app.config["MONGO_URI"] = os.getenv("MONGODB_URI") # Insert Database URI from MongoDB

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)