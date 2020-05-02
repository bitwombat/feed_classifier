#!/usr/bin/env python
import hashlib


def hash_titles(article_list):
    """Add a title-hash key to each article dict"""
    new_article_list = []
    for article in article_list:
        h = hashlib.sha256()
        h.update(article["title"].encode("utf-8"))
        article["title-hash"] = h.hexdigest()[0:7]
        new_article_list.append(article)
    return new_article_list
