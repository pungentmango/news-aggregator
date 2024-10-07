# rss_parse_service.py
import feedparser

def parse_feed(feed_url):
    """
    Main function to parse the feed and identify its type (RSS or Atom).
    Calls the appropriate parsing method based on the feed version.
    """
    feed = feedparser.parse(feed_url)

    # Check for feed type
    if feed.bozo:
        raise ValueError("Feed could not be parsed")

    articles = []
    
    # Loop through the feed entries (articles)
    for entry in feed.entries:
        # Extract attributes safely (handle missing fields)
        title = entry.get('title', 'No Title')
        link = entry.get('link', 'No Link')
        published = entry.get('published', 'No Published Date')
        creator = entry.get('dc_creator', 'No Creator')  # 'dc:creator' is commonly stored under 'dc_creator'
        description = entry.get('description', 'No Description')
        
        # Append the article attributes to the list
        articles.append({
            'title': title,
            'link': link,
            'published': published,
            'creator': creator,
            'description': description
        })
    
    return articles