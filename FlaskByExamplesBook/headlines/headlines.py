from flask import Flask, request
import feedparser
from flask import render_template
import json
import urllib.request as urllib


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'https://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://rss.iol.io/iol/news'}

DEFAULTS = {'publication': 'bbc', 'city': 'London, UK'}


@app.route('/')
def home():
    # get customized headlines, based on user input or default
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    # get customized weather based on user input or default
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)

    return render_template('home.html', articles=articles, weather=weather)


def get_weather(query):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}uk&units=metric&appid=a27886fec137fb6e69e4a5697fd918df'
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get('weather'):
        weather = {'description': parsed['weather'][0]['description'],
                'temperature': parsed['main']['temp'],
                'city': parsed['name'], 'country': parsed['sys']['country']}
    return weather


def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


if __name__ == '__main__':
    app.run(debug=True)
