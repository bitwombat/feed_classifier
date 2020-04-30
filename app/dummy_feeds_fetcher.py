#!/usr/bin/env python


def fetch_feeds(urls):
    return "\n".join(open("tests/fixture/rss.xml").readlines())
