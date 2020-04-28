#!/usr/bin/env python

from title_hasher import hash_titles


class TestTitleHasher:
    def test_title_hasher(self):
        assert hash_titles(
            [
                {"title": "A", "url": "Aurl"},
                {"title": "B", "url": "Burl"},
                {"title": "C", "url": "Curl"},
            ]
        ) == [
            {"title": "A", "title_hash": "559aead", "url": "Aurl"},
            {"title": "B", "title_hash": "df7e70e", "url": "Burl"},
            {"title": "C", "title_hash": "6b23c0d", "url": "Curl"},
        ]
