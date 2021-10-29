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

