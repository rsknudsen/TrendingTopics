import requests

def get_news_page(PAGE=1):
    API_KEY = 'b526abc1d7af430e8bafc94cbe20ad93'
    TOPIC = 'Denmark'
    SORTBY = 'popularity'
    FROM = '2019-02-04'
    TO = '2019-02-05'

    URL = 'https://newsapi.org/v2/everything'
    PARAMS = {'q': TOPIC,
              'from': FROM,
              'to': TO,
              'sortBy': SORTBY,
              'pageSize': 100,
              'page': PAGE,
              'apiKey': API_KEY}

    response = requests.get(url=URL, params=PARAMS).json()
    return response

def get_news():
    articles = list()

    PAGE = 0
    while True:
        PAGE += 1
        news_page = get_news_page(PAGE)
        status = news_page['status']
        if status == 'ok':
            articles += news_page['articles']
        else:
            print('Number of articles available:', len(articles))
            break
    return articles

if __name__ == '__main__':
    articles = get_news()