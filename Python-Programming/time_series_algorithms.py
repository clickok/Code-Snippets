#!python3
"""
Interesting algorithms for time series
"""


def EW_average(alpha):
    """ One-pass exponentially weighted average. """
    xhat = yield
    while True:
        x       = yield(xhat)
        xhat    = (1-alpha)*x + alpha*xhat

def EW_variance(alpha):
    """ One-pass exponentially weighted variance. """
    xhat = yield
    vhat = 1
    while True:
        x = yield(vhat)
        xhat = (1-alpha)*x + (alpha*xhat)
        vhat = (1-alpha)*(x - xhat)**2 + (alpha * vhat)

