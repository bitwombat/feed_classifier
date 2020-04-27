#!/usr/bin/env python
import hashlib


def body_fetcher(url_fetcher):
    def body_fetcher_applied(article):
        article["body"] = url_fetcher(article["link"])
        return article

    return body_fetcher_applied


def fetch_bodies(url_fetcher, articles):
    return list(map(body_fetcher(url_fetcher), articles))
