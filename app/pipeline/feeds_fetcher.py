#!/usr/bin/env python

from autocurry import autocurry


@autocurry
def fetch_feeds(feed_fetcher, urls):
    return list(map(feed_fetcher, urls))
