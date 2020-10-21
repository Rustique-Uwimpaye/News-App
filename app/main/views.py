from flask import render_template
from . import main
from ..requests import get_articles,get_sources

@main.route("/")
def index():
    
    return render_template("index.html")

@main.route("/articles/<name>")
def body(name):
    bbc=get_articles("abc-news")
    abc=get_articles("abc-news-au")
    aljazeera=get_articles("al-jazeera-english")
    technical=get_articles("ars-technical")

    return render_template("articles.html",name=name,bbc_news=bbc,abc_news=abc,aljazeera_n=aljazeera,tech=technical)

def news(headlines):
 