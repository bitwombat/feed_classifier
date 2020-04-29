#!/usr/bin/env python

# Articles are sorted at this point, so we'll be outputting by class for free.
#


def format_as_text(articles):
    out_str = ""
    class_str = ""
    if not articles:
        out_str = "No articles"
        return out_str
    for article in articles:
        # Output header if class has changed
        if not class_str == article["class"]:
            class_str = article["class"]
            out_str += class_str.capitalize() + " " + "=" * (14 - len(class_str)) + "\n"
        out_str += article["title"] + " : " + article["url"] + "\n"

    return out_str
