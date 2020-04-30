#!/usr/bin/env python

import os.path
from joblib import dump, load

PERSISTENCE_FILENAME = "title_hashes.db"


def init_or_load_title_hashes():
    if not os.path.exists(PERSISTENCE_FILENAME):
        title_hashes = []
        dump(title_hashes, PERSISTENCE_FILENAME)
    else:
        title_hashes = load(PERSISTENCE_FILENAME)
    return title_hashes


def have_seen(title_hashes):
    def have_seen_applied(title_hash):
        return title_hash in title_hashes

    return have_seen_applied


def mark_as_seen(title_hashes):
    def mark_as_seen_applied(articles):
        title_hashes.extend([article["title-hash"] for article in articles])
        dump(title_hashes, PERSISTENCE_FILENAME)
        return articles

    return mark_as_seen_applied
