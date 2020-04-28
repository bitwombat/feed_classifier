#!/usr/bin/env python


def remove_seen(tester, articles):
    return list(filter(lambda article: not tester(article["title_hash"]), articles))
