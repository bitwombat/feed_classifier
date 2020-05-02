#!/usr/bin/env python

def format_as_text(articles):
    """Turn the article list into a string, ready to print"""
    out_str = ""
    class_str = ""

    if not articles:
        out_str = "No articles"
        return out_str

    first_header = True

    for article in articles:
        # Output header if class has changed
        if not class_str == article["class"]:
            if not first_header:
                out_str += "\n"
            first_header = False
            class_str = article["class"]
            out_str += class_str.capitalize() + " " + "=" * (14 - len(class_str)) + "\n"
        out_str += article["title"] + " : " + article["url"] + "\n"

    return out_str
