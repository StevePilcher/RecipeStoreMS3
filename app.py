import os
from flask import Flask, render_template, redirect, request, session, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from config import Config
from flask_wtf import FlaskForm
from forms import LoginForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'recipe_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster.djr3q.mongodb.net/recipe_manager?retryWrites=true&w=majority'
app.config.from_object(Config)

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session ['username']
    return render_template('login.html', title='Home')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('signup.html')

@app.route('/create_recipe')
def create_recipe():
    return render_template('createrecipe.html', title='Create Recipe',
    categories=mongo.db.categories.find(),
    )

@app.route('/insert_recipe', methods=['POST','GET'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes'))

@app.route('/my_recipes')
def my_recipes():
    return render_template('myrecipes.html',
    recipes=mongo.db.recipes.find(),
    title='My Recipes')


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=categories)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_name':request.form.get('recipe_name'),
        'ingredients':request.form.get('ingredients'),
        'preparation_instructions':request.form.get('preparation_instructions'),
        'cooking_instructions':request.form.get('cooking_instructions'),
        'prep_time':request.form.get('prep_time'),
        'cook_time':request.form.get('cook_time')
    })
    return redirect(url_for('my_recipes'))

if __name__ == '__main__':
    app.secret_key= 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


