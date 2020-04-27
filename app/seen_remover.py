#!/usr/bin/env python
import hashlib


def remove_seen(tester, articles):
    return list(filter(lambda article: tester(article["title_hash"]), articles))
