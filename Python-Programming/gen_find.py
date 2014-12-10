#!python3
"""
Generator for finding files that match a unix-style pattern
"""

import fnmatch
import os

def gen_find(topdir, pattern):
    for path, dirlist, filelist in os.walk(topdir):
        for name in fnmatch.filter(filelist, pattern):
            yield os.path.join(path, name)
