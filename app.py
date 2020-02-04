import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes' # Insert Database Name
app.config["MONGO_URI"] = 'mongodb+srv://<username>:<password>@mycluster-kbtfd.gcp.mongodb.net/test?retryWrites=true&w=majority' # Insert Database URI from MongoDB

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)