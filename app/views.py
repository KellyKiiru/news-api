from flask import Flask
from flask import render_template
from app import app
from . import request

#The views with the necessary routing
@app.route('/')
def index():
    # Function that returns user to the index page  
    title = 'Home - Welcome to the home of worldwide news'

    return render_template('index.html', title = title)

