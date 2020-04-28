#!/usr/bin/env python
import trainer
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


def files_to_list(path):
    files_contents = []
    for path in glob(path + "/*"):
        with open(path) as f:
            files_contents.append(trainer.clean("\n".join(f.readlines())))
    return files_contents


def NB_classifier():
    news = files_to_list("training_data/news/")
    sports = files_to_list("training_data/sports/")

    model = make_pipeline(CountVectorizer(), MultinomialNB())

    data = news + sports
    labels = ["news"] * len(news) + ["sports"] * len(sports)
    model.fit(data, labels)

    def classifier_applied(article_text):
        return model.predict([article_text])[0]

    return classifier_applied
