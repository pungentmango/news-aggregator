from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

# List of RSS feeds to aggregate from
RSS_FEEDS = {
    'tech': 'https://www.wired.com/feed/rss',
    'world': 'http://feeds.bbci.co.uk/news/rss.xml',
    'business': 'https://www.cnbc.com/id/100003114/device/rss/rss.html'
}

def parse_rss(feed_url):
    """
    Fetch and parse RSS feed data.
    """
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
    
    return articles

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the News Aggregator API"})

@app.route('/news')
def get_news():
    """
    Aggregate news from multiple RSS feeds and return as JSON.
    """
    aggregated_news = {}
    
    for category, url in RSS_FEEDS.items():
        aggregated_news[category] = parse_rss(url)
    
    return jsonify(aggregated_news)

if __name__ == '__main__':
    app.run(debug=True)
