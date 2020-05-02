#!/usr/bin/env python
import re

# we'd like to turn into the 'word' "wed" instead of two words "we d"
# it's a guess whether or not this is the better approach.
apostrophes = re.compile(r"[\'’]")

# It seems important to know when money is being discussed. So $100,000 will
# turn into $.
letters_and_dollars = re.compile(r"[^A-Za-z$]+")


def clean(s):
    """Clean up article text to improve accuracy with the Bayesian classifier"""
    without_contractions = apostrophes.sub("", s)
    return re.sub(letters_and_dollars, " ", without_contractions).lower().strip()
