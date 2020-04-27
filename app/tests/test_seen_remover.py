#!/usr/bin/env python

from seen_remover import remove_seen


class TestSeenRemover:
    def getter(self, key):
        def getter_applied(item):
            return item[key]
        return getter_applied

    def seen_tester(self, hashval):
        if hashval == "df7e70e":
            return False
        return True

    def test_seen_remover(self):
        assert remove_seen(
            self.getter('title_hash'),
            self.seen_tester,
            [
                {"title": "A", "title_hash": "559aead", "link": "Alink"},
                {"title": "B", "title_hash": "df7e70e", "link": "Blink"},
                {"title": "C", "title_hash": "6b23c0d", "link": "Clink"},
            ],
        ) == [
            {"title": "A", "title_hash": "559aead", "link": "Alink"},
            {"title": "C", "title_hash": "6b23c0d", "link": "Clink"},
        ]
