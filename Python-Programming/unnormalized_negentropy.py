#!python3
"""
Compute the unnormalized negative entropy.

(Using "nat" units)
"""

import numpy as np

def negentropy(x):
    """ Negative unnormalized Shannon entropy"""
    return np.dot(x, np.log(x)) - np.sum(x)


def kl_divergence(x,y):
    """ Unnormalized Kullback-Leibler divergence """
    x, y = np.array(x), np.array(y)
    grad_y = np.log(y)
    return negentropy(x) - negentropy(y) - np.dot(grad_y, x - y)

def check_simplex_projection(x, n=1000):
    """
    Quickly try to find an approximate minimum of divergence for given x within
    the probability simplex.
    """
    x = np.array(x)
    xlength = len(x)
    assert(xlength == np.prod(x.shape)) # check that x is 1-D
    best_min = np.inf
    for i in range(n):
        y = np.random.random(xlength)
        y = y / np.sum(y) # normalize
        divergence = kl_divergence(x,y) # get divergence
        if divergence < best_min:
            xstar = y.copy()
            best_min = divergence
    return xstar, best_min