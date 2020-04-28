#!/usr/bin/env python

from autocurry import autocurry


def classify_one(NB_classifier):
    def classify_one_applied(article):
        article["class"] = NB_classifier(article["title"] + " " + article["body"])
        return article

    return classify_one_applied


@autocurry
def classify(NB_classifier, articles):
    return list(map(classify_one(NB_classifier), articles))
