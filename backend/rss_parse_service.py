# rss_parse_service.py
import feedparser
import dateutil.parser

def parse_feed(feed_url):
    """
    Main function to parse the feed and identify its type (RSS or Atom).
    Calls the appropriate parsing method based on the feed version.
    """
    feed = feedparser.parse(feed_url)

    # Check for feed type
    if feed.bozo:
        raise ValueError("Feed could not be parsed")

    feed_type = identify_feed_type(feed)
    
    if feed_type == 'rss':
        return parse_rss(feed)
    elif feed_type == 'atom':
        return parse_atom(feed)
    else:
        raise ValueError("Unknown feed type")

def identify_feed_type(feed):
    """
    Identify the type of feed (RSS or Atom) based on the feed's structure.
    """
    if 'rss' in feed and feed.version.startswith('rss'):
        return 'rss'
    elif 'feed' in feed and feed.version.startswith('atom'):
        return 'atom'
    return None

def parse_rss(feed):
    """
    Parse an RSS feed and extract articles.
    """
    articles = []
    
    for entry in feed.entries:
        title = entry.get('title', 'No title available')
        link = entry.get('link', 'No link available')
        published = entry.get('pubDate', 'No date available')
        
        try:
            published = dateutil.parser.parse(published).strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError):
            published = 'Unknown'

        creator = entry.get('dc:creator', entry.get('author', 'Unknown author'))
        description = entry.get('description', 'No description available')

        articles.append({
            'title': title,
            'link': link,
            'published': published,
            'creator': creator,
            'description': description
        })
    
    return articles

def parse_atom(feed):
    """
    Parse an Atom feed and extract articles.
    """
    articles = []
    
    for entry in feed.entries:
        title = entry.get('title', 'No title available')
        link = entry.get('link', 'No link available')
        published = entry.get('updated', 'No date available')
        
        try:
            published = dateutil.parser.parse(published).strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, TypeError):
            published = 'Unknown'

        creator = entry.get('author', [{'name': 'Unknown author'}])[0].get('name', 'Unknown author')
        description = entry.get('summary', 'No description available')

        articles.append({
            'title': title,
            'link': link,
            'published': published,
            'creator': creator,
            'description': description
        })
    
    return articles
