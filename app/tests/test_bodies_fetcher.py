#!/usr/bin/env python

from bodies_fetcher import fetch_bodies


class TestBodiesFetcher:
    def url_fetcher(self, url):
        if url == "http://A":
            return "A text"
        if url == "http://B":
            return "B text"
        if url == "http://C":
            return "C text"

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
                "body": "A text",
            },
            {
                "title": "B",
                "title_hash": "df7e70e",
                "link": "http://B",
                "body": "B text",
            },
            {
                "title": "C",
                "title_hash": "6b23c0d",
                "link": "http://C",
                "body": "C text",
            },
        ]
