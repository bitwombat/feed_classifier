#!/usr/bin/env python

from outputter import output


class TestOutputter:
    def test_outputter(self):
        assert (
            output(
                [
                    {
                        "title": "A",
                        "title_hash": "559aead",
                        "url": "http://A",
                        "body": "A body",
                        "class": "news",
                    },
                    {
                        "title": "B",
                        "title_hash": "df7e70e",
                        "url": "http://B",
                        "body": "B body",
                        "class": "news",
                    },
                    {
                        "title": "C",
                        "title_hash": "6b23c0d",
                        "url": "http://C",
                        "body": "C body",
                        "class": "sports",
                    },
                ]
            )
            == """News ==========
A : http://A
B : http://B
Sports ========
C : http://C
"""
        )
