#!/usr/bin/env python

from feed_classifier.cleaner import clean
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


def path_to_contents(path):
    """Reads contents of all files on the path into a list, one entry per file."""
    files_contents = []
    for path in glob(path + "/*"):
        with open(path) as f:
            files_contents.append(clean("\n".join(f.readlines())))
    return files_contents


def NB_classifier():
    """Trains and returns a naive Bayes classifier"""
    news = path_to_contents("training_data/news/")
    sports = path_to_contents("training_data/sports/")

    model = make_pipeline(CountVectorizer(), MultinomialNB())

    data = news + sports
    labels = ["news"] * len(news) + ["sports"] * len(sports)
    model.fit(data, labels)

    def classifier_applied(article_text):
        return model.predict([article_text])[0]

    return classifier_applied
