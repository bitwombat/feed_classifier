#!/usr/bin/env python


def remove_seen(have_seen, articles):
    return list(filter(lambda article: not have_seen(article["title_hash"]), articles))
