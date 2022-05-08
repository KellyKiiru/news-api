from . import main 
from ..request import *
from flask import render_template,request,redirect,url_for 
from ..models import *




#The views with the necessary routing
@main.route('/')
def home():
    tech_articles = get_article_by_top_headline('technology')
    all_articles = get_all_articles('all') 
    all_sources = get_sources()

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search',article=search_article))

    return render_template('index.html',tech_articles=tech_articles,all_articles=all_articles,all_sources=all_sources)


@main.route('/search/<article>')
def search(article):
    searched_articles_list = article.split(" ")
    article_name_format = "+".join(searched_articles_list)
    searched_articles = search_article(article_name_format)

    heading = article.capitalize()
    
    return render_template('found.html',searched_articles=searched_articles,heading=heading)



@main.route('/source/<source_name>')
def source(source_name):
    article_display = get_article_by_source(source_name)
    title = source_name.capitalize()

    return render_template('source.html', article_display=article_display,title=title )

@main.route('/sources')
def sources():
    all_sources = get_sources()

    return render_template('sources.html',all_sources=all_sources)