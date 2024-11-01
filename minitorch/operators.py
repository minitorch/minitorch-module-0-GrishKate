"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1


#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def neg(a):
    return - a


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    if a >= b:
        return a
    return b


def is_close(a, b):
    return abs(a - b) < 1e-2


def sigmoid(a):
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    return math.exp(a) / (1 + math.exp(a))


def relu(a):
    return max(a, 0)


def log(a):
    return math.log(a)


def exp(a):
    return math.exp(a)


def inv(a):
    return 1 / a


def log_back(a, b):
    return b / a


def inv_back(a, b):
    return -b / a ** 2


def relu_back(a, b):
    if a > 0:
        return b
    return 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(f, lst):
    return [f(lst[i]) for i in range(len(lst))]


def zipWith(f, lst1, lst2):
    return [f(lst1[i], lst2[i]) for i in range(len(lst1))]


def reduce(f, lst):
    if len(lst) == 0:
        return 0.0
    a = lst[0]
    for i in range(1, len(lst)):
        a = f(a, lst[i])
    return a


def negList(lst):
    return map(neg, lst)


def addLists(lst1, lst2):
    return zipWith(add, lst1, lst2)


def sum(lst):
    return reduce(add, lst)


def prod(lst):
    return reduce(mul, lst)
