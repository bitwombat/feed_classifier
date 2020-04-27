#!/usr/bin/env python

import trainer

class TestTraining:

    def test_cleaning(self):
        assert trainer.clean(r"One,Two, three four ; five.six seven. eight \"nine\" 'ten'") \
        == "one two three four five six seven eight nine ten"

        assert trainer.clean(r"we’ve we've") \
        == "weve weve"

        assert trainer.clean(r"’eleven ”twelve “thirteen") \
        == "eleven twelve thirteen"

        assert trainer.clean(r"&fourteen #fifteen") \
        == "fourteen fifteen"

        # If the article is talking about dollars, we leave that
        # symbol in
        assert trainer.clean(r"$sixteen (seventeen) 18eighteen :nineteen") \
        == "$sixteen seventeen eighteen nineteen"

    def test_enumerating(self):
        assert trainer.enumerate("A A A A B B B B C C D D D E F F") \
                == {'A' : 4, 'B' : 4, 'C' : 2, 'D' : 3, 'E' : 1, 'F' : 2}

