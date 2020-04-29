#!/usr/bin/env python

from feed_parser import parse_feeds


class TestFeedParser:
    def test_feed_parser(self):
        feeds = [
            "\n".join(open("tests/fixture/rss.xml").readlines()),
            "\n".join(open("tests/fixture/rss2.xml").readlines()),
        ]

        assert parse_feeds(feeds) == [
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
            {
                "title": "Need some good news? We can help",
                "url": "http://www.portnews.com.au/story/6739915/need-some-good-news-we-can-help/?src=rss",
            },
            {
                "title": "Vigilance is a must as COVID-19 restrictions start to ease",
                "url": "http://www.portnews.com.au/story/6739432/vigilance-is-a-must-as-covid-19-restrictions-start-to-ease/?src=rss",
            },
        ]
