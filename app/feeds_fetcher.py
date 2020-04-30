#!/usr/bin/env python

import requests

def fetch_feed(url):
    return requests.get(url).text


def fetch_feeds(urls):
    return list(map(fetch_feed, urls))
