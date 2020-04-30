#!/usr/bin/env python


def feed_fetcher(url):
    return "\n".join(open("tests/fixture/rss.xml").readlines())


def body_fetcher(url):
    return ""  # Haven't needed this yet. No full offline end-to-end test has been run.
