#!/usr/bin/env python

from pipeline.bodies_fetcher import fetch_bodies


class TestBodiesFetcher:
    def body_fetcher(self, url):
        if url == "http://A":
            return "A body"
        if url == "http://B":
            return "B body"
        if url == "http://C":
            return "C body"

    def test_bodies_fetcher(self):
        assert fetch_bodies(
            self.body_fetcher,
            [
                {"title": "A", "title-hash": "559aead", "url": "http://A"},
                {"title": "B", "title-hash": "df7e70e", "url": "http://B"},
                {"title": "C", "title-hash": "6b23c0d", "url": "http://C"},
            ],
        ) == [
            {
                "title": "A",
                "title-hash": "559aead",
                "url": "http://A",
                "body": "A body",
            },
            {
                "title": "B",
                "title-hash": "df7e70e",
                "url": "http://B",
                "body": "B body",
            },
            {
                "title": "C",
                "title-hash": "6b23c0d",
                "url": "http://C",
                "body": "C body",
            },
        ]
