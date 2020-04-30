#!/usr/bin/env python

from bs4 import BeautifulSoup


def parse_feed(feed):
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
    return sum(list(map(parse_feed, feeds)), [])
