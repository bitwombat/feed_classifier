#!/usr/bin/env python
import trainer
import pandas as pd
from glob import glob
from sklearn.feature_extraction.text import TfidfVectorizer

articles = []
for path in glob('training_data/news/*'):
    with open(path) as f:
        articles.append(trainer.clean('\n'.join(f.readlines())))

vec = TfidfVectorizer()

X = vec.fit_transform(articles)

#print(pd.DataFrame(X.toarray(), columns=vec.get_feature_names()))

print(trainer.clean("this, is good"))
