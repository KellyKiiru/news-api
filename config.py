## Configuration files 
import os
from distutils.debug import DEBUG

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&language=en&from=2022-04-16&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}