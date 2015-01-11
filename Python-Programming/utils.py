#python3
"""
A compendium of common, useful things.

Some of this is taken from, or otherwise inspired by Peter Norvig, at
`http://aima.cs.berkeley.edu/python/utils.html`
"""

import operator

try:
    reduce
except NameError:
    from functools import reduce

try: infinity
except NameError:
    inifinity = 1.0e400

# Functions on sequences
def unique(seq):
    return list(set(seq))

def product(numseq):
    """ Return the product of a sequence of numbers. """
    return reduce(operator.mul, numseq, 1)

def removeall(item, seq):
    """ 
    Returns a generator of the elements of `seq` that are not `==` to `item`.

    I was being 'clever' trying to use `type(seq)(x for x ...)` to ensure that
    the result was of the same type as `seq`, but it turns out that that's 
    not the smartest idea. (Hint: try it with `range`).
    """
    return (x for x in seq if x != item)

def count_if(pred, seq):
    """ 
    Count the number of elements of `seq` for which the predicate is true.
    """
    pass