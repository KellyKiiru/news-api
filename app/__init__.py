from flask import Flask

from app.main import views
from ..config import DevConfig



#initializing flask
app  = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
#configuration that store the news api key
app.config.from_pyfile('config.py')


#importing error and view files from app
from app.main import error 
