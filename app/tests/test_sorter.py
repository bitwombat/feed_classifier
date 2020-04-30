#!/usr/bin/env python

from pipeline.sorter import sort


class TestSorter:
    def test_sorter(self):
        assert sort(
            [
                {
                    "title": "A",
                    "title-hash": "559aead",
                    "url": "http://A",
                    "body": "A body",
                    "class": "Z",
                },
                {
                    "title": "B",
                    "title-hash": "df7e70e",
                    "url": "http://B",
                    "body": "B body",
                    "class": "Y",
                },
                {
                    "title": "C",
                    "title-hash": "6b23c0d",
                    "url": "http://C",
                    "body": "C body",
                    "class": "X",
                },
            ]
        ) == [
            {
                "title": "C",
                "title-hash": "6b23c0d",
                "url": "http://C",
                "body": "C body",
                "class": "X",
            },
            {
                "title": "B",
                "title-hash": "df7e70e",
                "url": "http://B",
                "body": "B body",
                "class": "Y",
            },
            {
                "title": "A",
                "title-hash": "559aead",
                "url": "http://A",
                "body": "A body",
                "class": "Z",
            },
        ]
