from flask import Flask

#initializing flask
app  = Flask(__name__)

#importing error and view files from app
from app import views,error 