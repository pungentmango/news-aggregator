# app.py
from flask import Flask, jsonify
from rss_parse_service import parse_feed

app = Flask(__name__)

# Example RSS feeds with different structures
RSS_FEEDS = {
    'tech': [
        'https://techcrunch.com/feed/',
        'https://www.theverge.com/rss/index.xml'
    ],
    'world': [
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'http://rss.cnn.com/rss/edition_world.rss'
    ],
    'business': [
        'https://www.cnbc.com/id/100003114/device/rss/rss.html',
        'http://feeds.reuters.com/reuters/businessNews'
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
