"""
Ways of memoizing things
"""


class Memoize():
    def __init__(self, fn):
        self.cache = {}
        self.fn = fn

    def __call__(self, *args):
        if args in self.cache:
            ret = self.cache[args]
        else:
            ret = self.fn(*args)
            self.cache[args] = ret 
        return ret 



"""
# We could try an example...
if __name__ == "__main__":
    # The basic recursive factorial function to be used in comparisons
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n-1)

    foo = Memoize(factorial)

    import functools
    @functools.lru_cache()
    def bar(n):
        if n <= 1:
            return 1
        else:
            return n * bar(n-1)


###############################################################################
>>> %timeit factorial(5)
1000000 loops, best of 3: 910 ns per loop

>>> %timeit foo
10000000 loops, best of 3: 522 ns per loop

>>> %timeit bar(5)
1000000 loops, best of 3: 1.78 µs per loop

>>> %timeit [factorial(i) for i in range(100)]
1000 loops, best of 3: 1.24 ms per loop

>>> %timeit [foo(i) for i in range(100)]
10000 loops, best of 3: 56.5 µs per loop

>>> %timeit [bar(i) for i in range(100)]
10000 loops, best of 3: 176 µs per loop
"""
