#!/usr/bin/env python
import hashlib

def remove_seen(getter, tester, lst):
    return list(filter(lambda x: tester(getter(x)), lst))
