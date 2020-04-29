#!/usr/bin/env python

import functools
from autocurry import autocurry


def compose(*functions):
    """ Functional composition """
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def pipe(pipe_input, functions):
    """ Same as compose, just different order, for more natural pipelining """
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)(
        pipe_input
    )


@autocurry
def tell_user(msg, fn, data):
    print(msg.format(fn(data)))
    return data


def id(x):
    return x
