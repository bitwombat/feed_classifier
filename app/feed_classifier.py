#!/usr/bin/env python

# Classifies articles in local news feeds as "news" or "sports", displaying
# only articles not seen before.
#
# Side note: Instead of storing a hash of each title, we could have saved the
# hassel of persisting all (and therefore having to clean out old articles in
# case a title was re-used in the future), by simply diff'ing with the previous
# output to get the new ones.  But, what if an article went off the feed, then
# came back on?  Diff would report it as new, but this possibly over-engineered
# solution won't be fooled.
#
# Instead of cleaning out old articles from stories, I could instead have combined the
# article id with the title for the hash - much more likely to be unique into
# the future. But this wouldn't work, because some stories that were in both
# feeds had the same title, but different story id's (and sometimes the same
# id). This would have caused them to be doubled-up on the output.

import functools
import requests
import sys

from persistence import init_or_load_title_hashes
from utils import compose, pipe, tell_user, id

# Pipeline components
from pipeline.feeds_fetcher import fetch_feeds
from pipeline.feeds_parser import parse_feeds
from pipeline.duplicate_remover import remove_duplicates
from pipeline.titles_hasher import hash_titles
from pipeline.seen_remover import remove_seen
from pipeline.bodies_fetcher import fetch_bodies
from pipeline.classifier import classify
from pipeline.sorter import sort
from persistence import mark_as_seen
from formatter import format_as_text


# Dependencies injected for testing purposes
# Note there's a 'dummy' module which has versions of the functions in
# `internet` that don't connect to the internet. For end-to-end testing.
# TODO:
# implement dummy versions of the persistence functions, also for testing.

from internet import feed_fetcher, body_fetcher
from NB_classifier import NB_classifier
from persistence import have_seen


def main():
    URLS = [
        "http://www.portnews.com.au/rss.xml",
        "https://www.wauchopegazette.com.au/rss.xml",
    ]

    title_hashes = init_or_load_title_hashes()

    print(
        pipe(
            URLS,
            (
                tell_user("Fetching {} feeds...", len),
                fetch_feeds(feed_fetcher),
                parse_feeds,
                tell_user("Found {} articles", len),
                remove_duplicates,
                tell_user("Of those, {} are unique", len),
                hash_titles,
                remove_seen(have_seen(title_hashes)),
                tell_user("{} are new", len),
                tell_user("Fetching article bodies...", id),
                fetch_bodies(body_fetcher),
                classify(NB_classifier()),
                sort,
                mark_as_seen(title_hashes),
                format_as_text,
            ),
        )
    )


if __name__ == "__main__":
    sys.exit(main())
