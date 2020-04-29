#!/usr/bin/env python

from formatter import format_as_text


class TestFormatter:
    def test_formatter(self):
        assert (
            format_as_text(
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
