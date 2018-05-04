import datetime
from rfeed import *
from dateutil.parser import parse

def get_rss_for_json(data):
    items = []
    for article in data['articles']:
        pubDate = datetime.datetime.now()
        try:
            pubDate = parse(article['publishedAt'])
        except:
            pass
        item = Item(
            	title = article['title'],
            	link = article['url'],
            	description = article['description'],
                author = article['author'],
                guid = Guid(article['url']),
            	pubDate = pubDate)
        items.append(item)

    feed = Feed(title = "Newsapi RSS Feed",
            	link = "https://newsapi.org",
            	description = "Newsapi",
            	language = "en-US",
            	lastBuildDate = datetime.datetime.now(),
            	items = items)

    return feed.rss()
