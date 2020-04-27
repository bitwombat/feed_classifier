#!/usr/bin/env python

from sorter import sort


class TestSorter:

    def test_sorter(self):
        assert sort(
            [
                {"title": "A", "title_hash": "559aead", "link": "http://A", "body": "A body", "class": "Z"},
                {"title": "B", "title_hash": "df7e70e", "link": "http://B", "body": "B body", "class": "Y"},
                {"title": "C", "title_hash": "6b23c0d", "link": "http://C", "body": "C body", "class": "X"},
            ],
        ) == [
            {
                "title": "C",
                "title_hash": "6b23c0d",
                "link": "http://C",
                "body": "C body",
                "class": "X",
            },
            {
                "title": "B",
                "title_hash": "df7e70e",
                "link": "http://B",
                "body": "B body",
                "class": "Y",
            },
            {
                "title": "A",
                "title_hash": "559aead",
                "link": "http://A",
                "body": "A body",
                "class": "Z",
            },
        ]
