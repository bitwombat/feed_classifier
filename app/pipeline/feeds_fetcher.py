#!/usr/bin/env python

from autocurry import autocurry


@autocurry
def fetch_feeds(feed_fetcher, urls):
    """Use the injected feed_fetcher function to fetch the passed urls
       feed_fetcher is a http client, or a file reader in testing.
    """
    return list(map(feed_fetcher, urls))
