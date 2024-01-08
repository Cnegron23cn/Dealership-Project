from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.car import Car
import os
import requests


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/save_search')
def save_search():
    if 'user_id' not in session:
        return render_template('/')
    data ={ 'id':session['user_id']}
    return render_template('/saved_searches.html', User = User.get_one(data))


@app.route('/dashboard_inventory')
def dash_inventory():
    if 'user_id' not in session:
        return render_template('/')
    return render_template('/inventory_dashboard.html')
