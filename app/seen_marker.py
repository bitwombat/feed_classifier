#!/usr/bin/env python


def mark_as_seen(marker, articles):
    map(lambda article: marker(article), articles)
    return articles
