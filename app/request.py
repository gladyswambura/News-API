from app import app
import urllib.request,json
from .models import news

News = news.News
 

api_key = app.config('NEWS_API_KEY')   #'da55160577bc4d3e82d05e4590bdded5'
base_url = app.config('NEWS_API_BASE_URL')  #'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns:
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = News(id, title, description, url, urlToImage, publishedAt)
            news_results.append(news_object)

    return news_results