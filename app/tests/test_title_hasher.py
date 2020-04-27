#!/usr/bin/env python

from title_hasher import hash_titles


class TestTitleHasher:
    def test_title_hasher(self):
        assert hash_titles(
            [
                {"title": "A", "link": "Alink"},
                {"title": "B", "link": "Blink"},
                {"title": "C", "link": "Clink"},
            ]
        ) == [
            {"title": "A", "title_hash": "559aead", "link": "Alink"},
            {"title": "B", "title_hash": "df7e70e", "link": "Blink"},
            {"title": "C", "title_hash": "6b23c0d", "link": "Clink"},
        ]
