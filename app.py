import os
from flask import Flask, render_template, redirect, request, url_for, flash, redirect
from flask_pymongo import PyMongo
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
@app.route('/index')
def index():
    user = {'username': 'Steve'}
    return render_template('base.html', title='Home', user=user)


@app.route('/create_recipe')
def create_recipe():
    user = {'username': 'Steve'}
    return render_template('createrecipe.html', title='Create Recipe', user=user,
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


@app.route('/update_recipe/<recipe_id>', methods=['POST', 'GET'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_name':request.form.get('recipe_name'),
        'ingredients':request.form.get('ingredients'),
        'preparaion_instructions':request.form.get('preparation_instructions'),
        'cooking_instructions':request.form.get('cooking_instructions'),
        'prep_time':request.form.get('prep_time'),
        'cook_time':request.form.get('cook_time')
    })
    return redirect(url_for('my_recipes'))

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


