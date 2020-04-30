#!/usr/bin/env python

from feeds_parser import parse_feeds


class TestFeedsParser:
    def test_feeds_parser(self):
        feeds = [
            "\n".join(open("tests/fixture/rss.xml").readlines()),
            "\n".join(open("tests/fixture/rss2.xml").readlines()),
        ]

        assert parse_feeds(feeds) == [
            {
                "title": "We remembered: Hastings unites to honour spirit of Anzac Day",
                "url": "http://www.portnews.com.au/story/6735034/we-remembered-hastings-unites-to-honour-spirit-of-anzac-day/?src=rss",
                "publish-date": "Sat, 25 Apr 2020 12:00:00 +1000",
            },
            {
                "title": "Who will you stand for? Our region honours its Anzacs",
                "url": "http://www.portnews.com.au/story/6734169/who-will-you-stand-for-our-region-honours-its-anzacs/?src=rss",
                "publish-date": "Sat, 25 Apr 2020 04:00:00 +1000",
            },
            {
                "title": "All the photos from the Ruby Princess departure at Port Kembla",
                "url": "http://www.portnews.com.au/story/6734211/all-the-photos-from-the-ruby-princess-departure-at-port-kembla/?src=rss",
                "publish-date": "Fri, 24 Apr 2020 21:38:00 +1000",
            },
            {
                "title": "Need some good news? We can help",
                "url": "http://www.portnews.com.au/story/6739915/need-some-good-news-we-can-help/?src=rss",
                "publish-date": "Wed, 29 Apr 2020 16:30:00 +1000",
            },
            {
                "title": "Vigilance is a must as COVID-19 restrictions start to ease",
                "url": "http://www.portnews.com.au/story/6739432/vigilance-is-a-must-as-covid-19-restrictions-start-to-ease/?src=rss",
                "publish-date": "Wed, 29 Apr 2020 16:00:00 +1000",
            },
        ]
