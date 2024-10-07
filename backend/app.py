# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from rss_parse_service import parse_feed

app = Flask(__name__)
CORS(app)

# Example RSS feeds with different structures
RSS_FEEDS = {
    'world': [
        'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'http://rss.cnn.com/rss/edition_world.rss',
        'http://feeds.reuters.com/reuters/worldNews',
        'https://www.aljazeera.com/xml/rss/all.xml'
    ],
    'politics': [
        'https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
        'http://feeds.bbci.co.uk/news/politics/rss.xml',
        'http://rss.cnn.com/rss/edition_politics.rss',
        'http://feeds.reuters.com/reuters/politicsNews',
        'https://www.aljazeera.com/xml/rss/feeds/americas.xml'
    ],
    'technology': [
        'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
        'http://feeds.bbci.co.uk/news/technology/rss.xml',
        'http://rss.cnn.com/rss/edition_technology.rss',
        'http://feeds.reuters.com/reuters/technologyNews',
        'https://www.aljazeera.com/xml/rss/feeds/technology.xml'
    ],
    'business': [
        'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
        'http://feeds.bbci.co.uk/news/business/rss.xml',
        'http://rss.cnn.com/rss/edition_business.rss',
        'http://feeds.reuters.com/reuters/businessNews',
        'https://www.aljazeera.com/xml/rss/feeds/business.xml'
    ]
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the News Aggregator API"})

@app.route('/news')
def get_news():
    """
    Aggregate news from multiple RSS feeds for each category and return as JSON.
    """
    aggregated_news = {}

    for category, urls in RSS_FEEDS.items():
        aggregated_news[category] = []
        for url in urls:
            try:
                articles = parse_feed(url)
                aggregated_news[category].extend(articles)
            except Exception as e:
                print(f"Error parsing {url}: {e}")

    return jsonify(aggregated_news)

if __name__ == '__main__':
    app.run(debug=True)
