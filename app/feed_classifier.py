#!/usr/bin/env python

import functools
import os.path
import requests
import sys

from bs4 import BeautifulSoup
from functools import partial
from joblib import dump, load
from pprint import pprint

from feed_parser import parse_feed
from titles_hasher import hash_titles
from seen_remover import remove_seen
from bodies_fetcher import fetch_bodies
from classifier import classify
from NB_classifier import NB_classifier
from sorter import sort
from outputter import output
from seen_marker import mark_as_seen


def compose(*functions):
    """ Functional composition """
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def pipe(pipe_input, functions):
    """ Same as compose, just different order, for more natural pipelining """
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)(
        pipe_input
    )


def fetch_feed(url):
    print("Fetching feed")
    #return "\n".join(open("tests/fixture/rss.xml").readlines())
    #return "\n".join(open("rss.xml").readlines())
    return requests.get(url).text


def body_fetcher(url):
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text, 'html.parser')
    return soup.find(itemprop="articleBody").text


PERSISTENCE_FILENAME = "title_hashes.joblib"


def tester():
    if not os.path.exists(PERSISTENCE_FILENAME):
        title_hashes = []
        dump(title_hashes, PERSISTENCE_FILENAME)
    else:
        title_hashes = load(PERSISTENCE_FILENAME)

    def tester_applied(title_hash):
        return title_hash in title_hashes

    return tester_applied


def saver():
    if not os.path.exists(PERSISTENCE_FILENAME):
        title_hashes = []
        dump(title_hashes, PERSISTENCE_FILENAME)
    else:
        title_hashes = load(PERSISTENCE_FILENAME)

    def mark_as_seen(articles):
        title_hashes.extend([article["title_hash"] for article in articles])
        dump(title_hashes, PERSISTENCE_FILENAME)
        return None

    return mark_as_seen


def main():
    url = "http://www.portnews.com.au/rss.xml"

    articles = pipe(
        url,
        (
            fetch_feed,
            parse_feed,
            hash_titles,
            partial(remove_seen, tester()),
            partial(fetch_bodies, body_fetcher),
            partial(classify, NB_classifier()),
            sort,
        ),
    )

    # Split the classified, sorted articles into two pipes
    print(output(articles))
    saver()(articles)


if __name__ == "__main__":
    sys.exit(main())
