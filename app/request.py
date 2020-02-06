from app import app
import urllib.request, json
from app.models.news import News
from app.models.article import Article

api_key = app.config['NEWS_API_KEY']


base_url = app.config['NEWS_API_BASE_URL']

article_url = app.config['ARTICLE_API_BASE_URL']

def get_news():
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    news_results = []
    for news in news_list:
        id = news.get('id')
        name = news.get('name')
        url = news.get('url')
        category = news.get('category')
        language = news.get('language')
        country = news.get('country')
        

        if id:
            news_object = News(id, name, url,category,language,country)
            news_results.append(news_object)

    return news_results


def get_newsarticle(source_id):
    get_news_details_url = article_url.format(source_id, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response['articles']:
            article_list = news_details_response['articles']
            news_object = process_articles(article_list)

    return news_object

def process_articles(article):

    news_objects = []

    for article_list in article:
        id = article_list.get('id')
        name = article_list.get('title')
        description = article_list.get('description')
        url = article_list.get('url')
        urlToImage = article_list.get('urlToImage')
        content = article_list.get('content')
        news_object = Article(id, name, description, url, urlToImage, content)
        
        news_objects.append(news_object)

    return news_objects

# def search_news(news_name):
#     search_news_url = 'https://api.thenewsdb.org/3/search/news?api_key={}&query={}'.format(api_key,news_name)
#     with urllib.request.urlopen(search_news_url) as url:
#         search_news_data = url.read()
#         search_news_response = json.loads(search_news_data)

#         search_news_results = None

#         if search_news_response['results']:
#             search_news_list = search_news_response['results']
#             search_news_results = process_results(search_news_list)


#     return search_news_results
