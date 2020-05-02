#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


def feed_fetcher(url):
    """HTTP url fetcher"""
    return requests.get(url).text


def body_fetcher(url):
    """Parse the article body HTML and grab the text of the article"""
    page_text = requests.get(url).text
    page = BeautifulSoup(page_text, "html.parser")
    return page.find(itemprop="articleBody").text
