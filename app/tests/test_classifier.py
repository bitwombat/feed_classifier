#!/usr/bin/env python

from pipeline.classifier import classify


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
            ],
        ) == [
            {
                "title": "A",
                "title-hash": "559aead",
                "url": "http://A",
                "body": "A body",
                "class": "news",
            },
            {
                "title": "B",
                "title-hash": "df7e70e",
                "url": "http://B",
                "body": "B body",
                "class": "news",
            },
            {
                "title": "C",
                "title-hash": "6b23c0d",
                "url": "http://C",
                "body": "C body",
                "class": "sports",
            },
        ]
