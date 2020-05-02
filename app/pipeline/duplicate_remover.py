#!/usr/bin/env python

seen = []


def not_seen_in_feed_yet(article):
    """Predicate to detect duplicate"""
    global seen
    have_seen_it = article["title"] in seen
    seen.extend([article["title"]])
    return not have_seen_it


def remove_duplicates(articles):
    """Remove the second article with the same title, which sometimes
       happens when two feeds draw from the same source."""
    return list(filter(not_seen_in_feed_yet, articles))
