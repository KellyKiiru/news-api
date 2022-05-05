from flask import Flask
from flask import render_template
from app import app
from .. import request 
from ..request import * 

#The views with the necessary routing
from flask import Flask
from flask import render_template,request,redirect,url_for
from app import app



#The views with the necessary routing
@app.route('/')
def home():
    all_articles = get_all_articles('all') 
    all_sources = get_sources()
    technology_articles = get_article_top_headline('technology')

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search',article=search_article))

    return render_template('index.html',all_articles=all_articles,all_sources=all_sources,technology_articles=technology_articles)
