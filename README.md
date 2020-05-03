# Bayesian RSS feed classifier
Downloads news articles from an RSS feed, categorises them based on naive Bayesian classification, then prints to screen and emails.

Only articles not seen before are shown.

This project makes use of the awesome [toolz](https://github.com/pytoolz/toolz)
library to organize everything as a pipeline of functions.

## Suitability
This is a personal project developed to process the Port News and Wauchope
Gazette newspapers in Australia. XML/HTML tags and properties will be specific
to those feeds, so you'll have to modify code for your particular feed. If
there's interest, complain about this in an issue, and I'll make everything
configurable.

It also only classifies articles as "news" or "sports".

## Training
Use `download_article.py` to download a particular article, based on URL, and
manually put the resulting file in either `training_data/news` or
`training_data/sports` dir.

## Other setup
`pip install -r requirements.txt`
Add your feed URLs and email to `feed_classifier.py`
Configure your email server in `pipeline/mail_sender.py`

## Running
Run `feed_classifier.py`, no arguments required.

## Unit tests

```
pip install -r requirements_dev.txt
python -m pytest
```
