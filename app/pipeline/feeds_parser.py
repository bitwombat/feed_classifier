#!/usr/bin/env python

from bs4 import BeautifulSoup


def parse_feed(feed):
    """Parse the feed XML into a list of hashes of just the data we need"""
    articles = []
    soup = BeautifulSoup(feed, "lxml-xml")
    items = soup.find_all("item")
    for item in items:
        articles.append(
            {
                "title": item.title.string,
                "url": item.link.string,
                "publish-date": item.pubDate.string,
            }
        )
    return articles


def parse_feeds(feeds):
    """Merge multiple feeds into one list
       This clever use of sum, instead of reduce, works
       because lists are monoids."""
    return sum(list(map(parse_feed, feeds)), [])
