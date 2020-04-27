#!/usr/bin/env python
import trainer
import pandas as pd
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer

# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Note: Tried pickling via the joblib module, but it was actually slower for
# this small training set.
#


def files_to_list(path):
    files_contents = []
    for path in glob(path + "/*"):
        with open(path) as f:
            files_contents.append(trainer.clean("\n".join(f.readlines())))
    return files_contents


news = files_to_list("training_data/news/")
sports = files_to_list("training_data/sports/")

model = make_pipeline(CountVectorizer(), MultinomialNB())
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())

data = news + sports
labels = ["news"] * len(news) + ["sports"] * len(sports)
model.fit(data, labels)

# Print predictions for the sports files we just trained on.
# You'd expect perfect answers, but with the TfidfVectorizer,
# it always guesses sports, even for news/*.
#
# for path in glob("training_data/sports/*"):
#    with open(path) as f:
#        print(model.predict([trainer.clean("\n".join(f.readlines()))]))

# Print a map showing the predicted vs. true labels. Should only have values on
# the diagonals.

predicted_labels = model.predict(data)

mat = confusion_matrix(labels, predicted_labels)
sns.set()
sns.heatmap(
    mat.T,
    square=True,
    annot=True,
    fmt="d",
    cbar=False,
    xticklabels=["news", "sports"],
    yticklabels=["news", "sports"],
)
plt.xlabel("true label")
plt.ylabel("predicted label")
plt.show()
