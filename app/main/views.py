from flask import render_template
from . import main
from ..requests import news,sources,get_articles,get_sources

@main.route("/")
def index():
    latest_news=news("latest-headlines")
    print(top_news)
    source=sources("sources")
    return render_template("index.html",latest_headline=top_news,sources=source)

@main.route("/articles/<name>")
def body(name):
    bbc=get_articles("abc-news")
    abc=get_articles("abc-news-au")
    aljazeera=get_articles("al-jazeera-english")
    technical=get_articles("ars-technical")

    return render_template("articles.html",name=name,bbc_news=bbc,abc_news=abc,aljazeera_n=aljazeera,tech=technical)
