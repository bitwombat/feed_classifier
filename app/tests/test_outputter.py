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
            )
            == """News ==========
A : http://A
B : http://B
Sports ========
C : http://C
"""
        )
