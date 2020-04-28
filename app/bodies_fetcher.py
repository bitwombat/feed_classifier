#!/usr/bin/env python
import hashlib
from autocurry import autocurry


def body_fetcher(url_fetcher):
    def body_fetcher_applied(article):
        article["body"] = url_fetcher(article["url"])
        return article

    return body_fetcher_applied


@autocurry
def fetch_bodies(url_fetcher, articles):
    return list(map(body_fetcher(url_fetcher), articles))
