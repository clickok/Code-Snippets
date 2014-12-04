#!python3
"""
Calculate the hypergeometric distribution.

That is, the probability of `x` successes in `n` draws without replacement from
a finite population of size `N` containing exactly `K` total successes.
"""

import argparse
from functools import reduce
import sys

def binom(n,k):
    """ Compute `n` choose `k` """
    numer = reduce(lambda x, y: x*y, range(n-k+1, n+1), 1)
    denom = reduce(lambda x, y: x*y, range(1, k+1), 1)
    return numer/denom

def hypergeometric(x, T, n, K):
    """
    Calculate the hypergeometric pmf

    Parameters
    ----------
    x : int 
        number of successes
    T : int
        total size of population from which to draw from
    n : int 
        number of trials drawn
    K : int 
        total number of successes in population

    Returns
    -------
    pmf : int 
        The p.m.f. at `x` for the hypergeometric distribution
    """
    xCK     = binom(K, x)
    n_xCT_K = binom(T-K, n-x)
    TCn     = binom(T, n)

    return (xCK * n_xCT_K)/TCn 

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int, help="number of successes")
    parser.add_argument('T', type=int, help="total size of population")
    parser.add_argument('n', type=int, help="number of trials")
    parser.add_argument('k', type=int, help="total number of successes in population")

    args = parser.parse_args()
    print(hypergeometric(args.x, args.T, args.n, args.k))

if __name__ == "__main__":
    main(sys.argv)