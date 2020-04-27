#!/usr/bin/env python

from seen_marker import mark_as_seen


class TestSeenMarker:
    def marker(self, title_hash):
        return None

    def test_seen_marker(self):
        # UUT should pass input data through unchanged. Side-effect only.
        assert mark_as_seen(
            self.marker,
            [
                {"some stuff"},
                {"title": "doesn't matter what"},
                {"title": "must pass thru"},
            ],
        ) == [
            {"some stuff"},
            {"title": "doesn't matter what"},
            {"title": "must pass thru"},
        ]
