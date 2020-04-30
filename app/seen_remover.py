#!/usr/bin/env python

from autocurry import autocurry


@autocurry
def remove_seen(have_seen, articles):
    return list(filter(lambda article: not have_seen(article["title-hash"]), articles))
