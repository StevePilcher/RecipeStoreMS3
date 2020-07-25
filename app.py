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


@app.route('/my_recipes')
def my_recipes():
    user = {'username': 'Tony'}
    return render_template('myrecipes.html',
    recipes=mongo.db.recipes.find(),
    title='My Recipes', user=user)


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


