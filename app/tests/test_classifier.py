#!/usr/bin/env python

from classifier import classify


class TestClassifier:
    def NB_classifier(self, text):
        if text == "A A body":
            return "news"
        if text == "B B body":
            return "news"
        if text == "C C body":
            return "sports"

    def test_classifier(self):
        assert classify(
            self.NB_classifier,
            [
                {"title": "A", "title_hash": "559aead", "link": "http://A", "body": "A body"},
                {"title": "B", "title_hash": "df7e70e", "link": "http://B", "body": "B body"},
                {"title": "C", "title_hash": "6b23c0d", "link": "http://C", "body": "C body"},
            ],
        ) == [
            {
                "title": "A",
                "title_hash": "559aead",
                "link": "http://A",
                "body": "A body",
                "class": "news",
            },
            {
                "title": "B",
                "title_hash": "df7e70e",
                "link": "http://B",
                "body": "B body",
                "class": "news",
            },
            {
                "title": "C",
                "title_hash": "6b23c0d",
                "link": "http://C",
                "body": "C body",
                "class": "sports",
            },
        ]
