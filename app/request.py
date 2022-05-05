import urllib.request,json
from .models import *

# api key
api_key = None
# news base url
base_url = None


def make_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    pass


def get_all_articles(query):
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(query,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results

def get_article_by_top_headline(category):
    
    get_articles_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results

def process_results(articles_list):
    articles_results = []
    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publisheAt')
        content = article.get('content')
        
        if urlToImage:
            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(article_object)

    return articles_results

def process_results_sources(sources_list):
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        url = source.get('url')

        source_obj = Source(id,name,url)
        sources_results.append(source_obj)
    return sources_results

def get_sources():
    get_sources_url = 'https://newsapi.org/v2/sources?&apiKey={}'.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results_sources(sources_results_list)

    return sources_results 

def search_article(article):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(article,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)
    return search_article_results

def get_article_everything(query):
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&from=2022-04-30&language=en&sortBy=publishedAt&apiKey={}'.format(query,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results

