#!/usr/bin/env python

from seen_remover import remove_seen


class TestSeenRemover:
    def have_seen(self, hashval):
        return hashval == "df7e70e"

    def test_seen_remover(self):
        assert remove_seen(
            self.have_seen,
            [
                {"title": "A", "title-hash": "559aead", "url": "Aurl"},
                {"title": "B", "title-hash": "df7e70e", "url": "Burl"},
                {"title": "C", "title-hash": "6b23c0d", "url": "Curl"},
            ],
        ) == [
            {"title": "A", "title-hash": "559aead", "url": "Aurl"},
            {"title": "C", "title-hash": "6b23c0d", "url": "Curl"},
        ]
