#!/usr/bin/env python

from feed_classifier.cleaner import clean, enumerate


class TestCleaner:
    def test_cleaning(self):
        assert (
            clean(r"One,Two, three four ; five.six seven. eight \"nine\" 'ten'")
            == "one two three four five six seven eight nine ten"
        )

        assert clean(r"we’ve we've") == "weve weve"

        assert clean(r"’eleven ”twelve “thirteen") == "eleven twelve thirteen"

        assert clean(r"&fourteen #fifteen") == "fourteen fifteen"

        # If the article is talking about dollars, we leave that
        # symbol in
        assert (
            clean(r"$sixteen (seventeen) 18eighteen :nineteen")
            == "$sixteen seventeen eighteen nineteen"
        )

    def test_enumerating(self):
        assert enumerate("A A A A B B B B C C D D D E F F") == {
            "A": 4,
            "B": 4,
            "C": 2,
            "D": 3,
            "E": 1,
            "F": 2,
        }
