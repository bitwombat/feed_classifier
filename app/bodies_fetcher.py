#!/usr/bin/env python
from autocurry import autocurry


@autocurry
def pop_body_into_article(body_fetcher, article):
    article["body"] = body_fetcher(article["url"])
    return article


@autocurry
def fetch_bodies(body_fetcher, articles):
    return list(map(pop_body_into_article(body_fetcher), articles))
