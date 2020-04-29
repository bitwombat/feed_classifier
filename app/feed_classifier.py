#!/usr/bin/env python

import functools
import requests
import sys

from bs4 import BeautifulSoup
from pprint import pprint

from persistence import init_or_load_title_hashes, have_seen, mark_as_seen
from utils import compose, pipe, tell_user, id

from feed_parser import parse_feeds
from duplicate_remover import remove_duplicates
from titles_hasher import hash_titles
from seen_remover import remove_seen
from bodies_fetcher import fetch_bodies
from classifier import classify
from NB_classifier import NB_classifier
from sorter import sort
from formatter import format_as_text


def fetch_feed(url):
    # return "\n".join(open("tests/fixture/rss.xml").readlines())
    # return "\n".join(open("rss.xml").readlines())
    return requests.get(url).text

def fetch_feeds(urls):
    return list(map(fetch_feed, urls))


def body_fetcher(url):
    page_text = requests.get(url).text
    page = BeautifulSoup(page_text, "html.parser")
    return page.find(itemprop="articleBody").text


def main():
    URLS = ["http://www.portnews.com.au/rss.xml",
            "https://www.wauchopegazette.com.au/rss.xml"]

    title_hashes = init_or_load_title_hashes()

    print(
        pipe(
            URLS,
            (
                tell_user("Fetching feed...", id),
                fetch_feeds,
                parse_feeds,
                tell_user("Found {} articles in feed", len),
                remove_duplicates,
                tell_user("Of those, {} are unique", len),
                hash_titles,
                remove_seen(have_seen(title_hashes)),
                tell_user("{} articles are new", len),
                tell_user("Fetching article bodies...", id),
                fetch_bodies(body_fetcher),
                classify(NB_classifier()),
                sort,
                mark_as_seen(title_hashes),
                format_as_text,
            ),
        )
    )


if __name__ == "__main__":
    sys.exit(main())
