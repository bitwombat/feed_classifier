#!/usr/bin/env python

import os.path
import json
import re
import calendar
from datetime import datetime
from toolz.itertoolz import pluck


PERSISTENCE_FILENAME = "title_hashes.json"

date_re = re.compile(r"^\w+, (\d+) (\w+) (\d+) (\d+):(\d+):(\d+)")


def is_fresh(datestr):
    """Predicate that returns True if the date is less than 60 days ago"""
    conv = {v: k for k, v in enumerate(calendar.month_abbr)}
    day, month, year, hour, minute, second = date_re.findall(datestr)[0]
    this_dt = datetime(
        int(year), conv[month], int(day), int(hour), int(minute), int(second)
    )
    now = datetime.today()
    diff = now - this_dt
    return diff.days < 60


def retire_old_hashes(titles):
    """Filters out any saved hashes that are more than 60 days old"""
    return list(filter(lambda x: is_fresh(x[1]), titles))


def have_seen(title_hashes):
    """Returns predicate function for determining if a title has been seen before"""
    def have_seen_applied(title_hash):
        return title_hash in pluck(0, title_hashes)

    return have_seen_applied


def load_title_hashes():
    """Loads database of seen articles from file on disk"""
    if not os.path.exists(PERSISTENCE_FILENAME):
        title_hashes = []
    else:
        with open(PERSISTENCE_FILENAME, "r") as fp:
            title_hashes = list(json.load(fp))
        title_hashes = retire_old_hashes(title_hashes)
    return title_hashes


def mark_as_seen(title_hashes):
    """Saves database of seen articles to file on disk"""
    def mark_as_seen_applied(articles):
        title_hashes.extend(
            [(article["title-hash"], article["publish-date"]) for article in articles]
        )
        with open(PERSISTENCE_FILENAME, "w") as fp:
            json.dump(title_hashes, fp)

        return articles

    return mark_as_seen_applied
