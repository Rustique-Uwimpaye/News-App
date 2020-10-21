import urllib.request,json
from .models import News,Sources,Articles

# Getting api key
api_key=None
# Getting the news base url
base_url=None
# Getting the source url
source_url=None
# Getting the article url
article_url=None

def configure_request(app):
    global api_key,base_url,source_url,article_url
    api_key=app.config["NEWS_API_KEY"]
    base_url=app.config["NEWS_API_BASE_URL"]
    source_url=app.config["NEWS_BASE_URL"]
    article_url=app.config["NEWS_ARTICLE_API"]

def get_articles(name):
    get_articles_url=article_url.format(name,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        article_data=url.read()
        article_response=json.loads(article_data)

        article_object=None;

        if article_response['articles']:
            at_result_list=article_response["articles"]
            at_results=process_articles(at_result_list)
    return at_results


def process_articles(article_list):
    article_results=[]
    for article in article_list:
        title=article.get("title")
        description=article.get("description")
        urlToImage=article.get("urlToImage")
        url=article.get("url")
        publishedAt=article.get("publishedAt")

        article_object=Articles(title,description,urlToImage,url,publishedAt)
        article_results.append(article_object)

    return article_results

def get_sources(name):
    get_articles_details_url=article_url.format(name,api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        news_details_data=url.read();
        news_details_response=json.loads(news_details_data)

        news_object=None
        if news_details_response:
            title=news_details_response.get("title")
            description=news_details_response.get("description")
            urlToImage=news_details_response.get("urlToImage")
            url=news_details_response.get("url")
            publishedAt=news_details_response.get("publishedAt")

            news_object=Articles(title,description,url,urlToImage,publishedAt)
    return news_object
