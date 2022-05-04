from flask import Flask
from flask import render_template
from app import app


#The views with the necessary routing
@app.route('/')
def index():
    
    title = 'Home - Welcome to the home of worldwide news'
    # Function that returns user to the index page
    return render_template('index.html', title = title)
