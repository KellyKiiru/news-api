from flask import Flask
from app.config import DevConfig

#initializing flask
app  = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)

#importing error and view files from app
from app import views,error 
