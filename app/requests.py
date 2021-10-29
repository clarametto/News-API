import urllib.request
import json
from app.models import *

api_key=''

base_url=None

articles_base_url=None

def configure_request(app):
    global api_key, base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    article_url = app.config['ARTICLE_URL']

def get_news_source():
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = 'https://newsapi.org/v2/sources?apiKey={}'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_results_list):
    news_results= []
    for news_item in news_results_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_object =News(id, name, description,url,category,language,country)
            news_results.append(news_object)
    return news_results


def get_article(id):
    get_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id)

    article_result= None
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        print (get_article_data)
        if get_article_response['articles']:
            article_list = get_article_response['articles']
            article_result = process_article(article_list)

    return article_result


def process_article(article_list):
    article_response= []
    for article in article_list:
            id = article.get('id')
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('piblishedAt')
            if urlToImage:
                article_result =Articles(id, author,title, description,url,urlToImage,publishedAt)
                article_response.append(article_result)
    return article_response


def get_articles_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(
        category)
    # get_articles_url = base_url_articles.format(source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # load the data into a json object
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results  # return the results

def process_results_articles (articles_results_list):
    articles_results = []
    for article in articles_results_list:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('piblishedAt')
        if urlToImage:
            article_object = Articles(id, author,title, description,url,urlToImage,publishedAt)
            articles_results.append(article_object)
    return articles_results