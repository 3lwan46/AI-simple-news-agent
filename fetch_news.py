import feedparser
from config import RSS_FEEDS, TOP_N

def get_news():
    """
    Fetch top news from RSS feeds.
    Returns a list of dicts with 'title' and 'link'.
    """
    top_news = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:TOP_N]:
            top_news.append({
                "title": entry.title,
                "link": entry.link
            })
    return top_news
