#!/usr/bin/env python

# Articles are sorted at this point, so we'll be outputting by class for free.
#


def output(articles):
    out_str = ""
    class_str = ""
    for article in articles:
        # Output header if class has changed
        if not class_str == article["class"]:
            class_str = article["class"]
            out_str += class_str.capitalize() + " " \
                + "=" * (14 - len(class_str)) + "\n"
        out_str += article["title"] + " : " + article["link"] + "\n"

    return out_str
