#!/usr/bin/env python

seen = []


def not_seen_in_feed_yet(article):
    global seen
    have_seen_it = article["title"] in seen
    seen.extend([article["title"]])
    return not have_seen_it


def remove_duplicates(articles):
    return list(filter(not_seen_in_feed_yet, articles))
