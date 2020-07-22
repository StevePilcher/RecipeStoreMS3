import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster.djr3q.mongodb.net/recipe_manager?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/base')
def index():
    user = {'username': 'Steve'}
    return render_template('base.html', title='Home', user=user)

@app.route('/my_recipes')
def my_recipes():
    user = {'username': 'Tony'}
    return render_template('myrecipes.html',
    recipes=mongo.db.recipes.find(),
    title='My Recipes', user=user)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')),
    debug=True)
