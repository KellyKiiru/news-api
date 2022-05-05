from flask import Flask
from .config import DevConfig

#initializing flask
app  = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
#configuration that store the news api key
app.config.from_object('config.py')


#importing error and view files from app
from app import views,error 
