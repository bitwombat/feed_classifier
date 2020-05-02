#!/usr/bin/env python
from autocurry import autocurry


@autocurry
def pop_body_into_article(body_fetcher, article):
    article["body"] = body_fetcher(article["url"])
    return article


@autocurry
def fetch_bodies(body_fetcher, articles):
    """Use the injected body_fetcher function to fetch the body of articles.
    This function will be a http client during normal operation, or a file
    reader during testing."""

    return list(map(pop_body_into_article(body_fetcher), articles))
