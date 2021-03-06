#!/usr/bin/env python


def sort(articles):
    """Sorts the articles based on classification
    Let's just be stupid about this. Assume just two classes, and,
    conveniently, 'sports' sorts last.
    """
    return sorted(articles, key=lambda article: article["class"])
