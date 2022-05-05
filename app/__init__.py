'''
import bootstrap and configurations
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    
    #initializing flask
    app  = Flask(__name__)

    #setting up configuration
    app.config.from_object(config_options[config_name])
    
    # Initializing bootstrap
    bootstrap.init_app(app) 
    
    # Register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .request import make_request
    make_request(app) 

    return app