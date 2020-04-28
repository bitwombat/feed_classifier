#!/usr/bin/env python

import requests
import sys
import re

from bs4 import BeautifulSoup


def body_fetcher(url):
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text, "html.parser")
    return soup.find(itemprop="articleBody").text


def main():

    if not len(sys.argv) == 2:
        print("Usage: download_article <url>")
        return 1

    url = sys.argv[1]
    body = body_fetcher(url)

    fname = url.split("/")[4] + ".art"

    with open(fname, "w") as fp:
        fp.write(body)


if __name__ == "__main__":
    sys.exit(main())
