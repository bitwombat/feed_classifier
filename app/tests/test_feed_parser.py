#!/usr/bin/env python

from feed_parser import parse_feed


class TestFeedParser:
    def test_feed_parser(self):
        feed = "\n".join(open("tests/fixture/rss.xml").readlines())
        assert parse_feed(feed) == [
            {
                "title": "We remembered: Hastings unites to honour spirit of Anzac Day",
                "url": "http://www.portnews.com.au/story/6735034/we-remembered-hastings-unites-to-honour-spirit-of-anzac-day/?src=rss",
            },
            {
                "title": "Who will you stand for? Our region honours its Anzacs",
                "url": "http://www.portnews.com.au/story/6734169/who-will-you-stand-for-our-region-honours-its-anzacs/?src=rss",
            },
            {
                "title": "All the photos from the Ruby Princess departure at Port Kembla",
                "url": "http://www.portnews.com.au/story/6734211/all-the-photos-from-the-ruby-princess-departure-at-port-kembla/?src=rss",
            },
        ]
