from flask import render_template

from app.models import Articles
from . import main
from ..requests import get_article, get_articles_category, get_news_source


@main.route('/')
def index():
    results = get_news_source()
    articles = get_articles_category('entertainment')

    return render_template(index.html, results=results, articles=articles)

