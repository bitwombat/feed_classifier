#!/usr/bin/env python

from seen_remover import remove_seen


class TestSeenRemover:

    def have_seen(self, hashval):
        return hashval == "df7e70e"

    def test_seen_remover(self):
        assert remove_seen(
            self.have_seen,
            [
                {"title": "A", "title_hash": "559aead", "link": "Alink"},
                {"title": "B", "title_hash": "df7e70e", "link": "Blink"},
                {"title": "C", "title_hash": "6b23c0d", "link": "Clink"},
            ],
        ) == [
            {"title": "A", "title_hash": "559aead", "link": "Alink"},
            {"title": "C", "title_hash": "6b23c0d", "link": "Clink"},
        ]
