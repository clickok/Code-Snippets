#!python3
"""
A quick script to unpickle a file that has been pickled using Python 2
"""

import pickle

def load(path, *args, **kwargs):
    kwargs['encoding'] = 'latin1'
    return pickle.load(open(path, 'rb'), *args, **kwargs)