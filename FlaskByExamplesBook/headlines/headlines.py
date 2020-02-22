from flask import Flask, request
import feedparser
from flask import render_template
import json
import urllib2
import urllib


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'https://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://rss.iol.io/iol/news'}


def get_weather(query):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={},\
                uk&units=metric&appid=a27886fec137fb6e69e4a5697fd918df'
    query = urllib.quote(query)
    url = api_url.format(query)


@app.route('/')
def get_news():
    query = request.args.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    # first_article = feed['entries'][0]
    return render_template('home.html', articles=feed['entries'])

if __name__ == '__main__':
    app.run(debug=True)
