#!/usr/bin/env python

from duplicate_remover import remove_duplicates


# Multiple local news feeds may publish the same story.
#
class TestDuplicateRemover:
    def test_duplicate_remover(self):
        feeds = [
            "\n".join(open("tests/fixture/rss.xml").readlines()),
            "\n".join(open("tests/fixture/rss2.xml").readlines()),
        ]

        assert remove_duplicates(
            [
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
                    "title": "Who will you stand for? Our region honours its Anzacs",
                    "url": "DUPLICATE http://www.wauchopegazette.com.au/story/6734169/who-will-you-stand-for-our-region-honours-its-anzacs/?src=rss",
                },
                {
                    "title": "All the photos from the Ruby Princess departure at Port Kembla",
                    "url": "DUPLICATE http://www.wauchopegazette.com.au/story/6734211/all-the-photos-from-the-ruby-princess-departure-at-port-kembla/?src=rss",
                },
            ]
        ) == [
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
