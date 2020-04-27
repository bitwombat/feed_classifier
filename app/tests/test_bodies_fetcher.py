#!/usr/bin/env python

from bodies_fetcher import fetch_bodies


class TestBodiesFetcher:
    def url_fetcher(self, url):
        if url == "http://A":
            return "A body"
        if url == "http://B":
            return "B body"
        if url == "http://C":
            return "C body"

    def test_bodies_fetcher(self):
        assert fetch_bodies(
            self.url_fetcher,
            [
                {"title": "A", "title_hash": "559aead", "link": "http://A"},
                {"title": "B", "title_hash": "df7e70e", "link": "http://B"},
                {"title": "C", "title_hash": "6b23c0d", "link": "http://C"},
            ],
        ) == [
            {
                "title": "A",
                "title_hash": "559aead",
                "link": "http://A",
                "body": "A body",
            },
            {
                "title": "B",
                "title_hash": "df7e70e",
                "link": "http://B",
                "body": "B body",
            },
            {
                "title": "C",
                "title_hash": "6b23c0d",
                "link": "http://C",
                "body": "C body",
            },
        ]
