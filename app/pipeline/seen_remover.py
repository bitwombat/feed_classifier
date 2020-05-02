#!/usr/bin/env python

from autocurry import autocurry


@autocurry
def remove_seen(have_seen, articles):
    """Remove articles that have been seen before"""
    return list(filter(lambda article: not have_seen(article["title-hash"]), articles))
