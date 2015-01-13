#!python3
"""
A quick script for getting the URLs of currently Chromium windows using 
Apple's appscript and the associated Python bindings.

Tab attributes
--------------
T.URL.set()

Tab methods
-----------
T.id() -- gets the id
T.properties() -- title, URL, loading, class, id
T.reload() -- reloads the tab
T.title() -- gets the title
T.URL() -- gets the URL


Window methods
--------------
W.active_tab_id()

Window "list" methods
---------------------
Chromium.windows.count() --  how many windows
Chromium.windows.first -- first

"""

import appscript as app
import argparse
import sys

from functools import reduce

def main(argv):
    # Argument parsing
    parser = argparse.ArgumentParser(description='Get Chromium Tabs')
    parser.add_argument('--windows', 
                         action='store_true',
                         help='Print window IDs and titles')
    parser.add_argument('--mode', default='url', 
                        help='Mode to use for tab printing (url, title, or all)')
    parser.add_argument('win_ids', nargs='*', 
                         help='Only print tabs from windows with these IDs')
    args = parser.parse_args()

    if args.windows:
        print_windows()
    else:
        win_ids = [int(x) for x in args.win_ids]
        tabs = get_tabs(win_ids)
        print_tabs(tabs, mode=args.mode)

    
def print_windows():
    """ Print the window titles and ids, for convenience """
    C = app.app('Chromium')
    if C.windows.count():
        for w in C.windows():
            print(w.id(), '\t', w.title()[:min(70, len(w.title()))])

def get_tabs(win_ids=None):
    """
    Get all tabs, or only the tabs within a specific list of windows,
    returning an iterable of the appscript tab objects.
    """
    C = app.app('Chromium')
    windows  = C.windows()
    
    # Filter the windows if win_ids specified
    if win_ids:
        windows = filter(lambda x: x.id() in win_ids, windows)
    
    # Get the tabs
    tabs = reduce(lambda x, y: x + y.tabs(), windows, [])
    return tabs

def print_tabs(tabs, mode='url'):
    """
    Given an iterable of tabs, print information about them.

    Parameters
    ----------
    mode : str
        url -- just print the URL (default)
        title -- just print the title
        all -- print id, title, and url
    """
    mode = mode.strip().lower()

    if mode == 'url':
        for t in tabs:
            print(t.URL())
    elif mode == 'title':
        for t in tabs:
            print(t.title())
    elif mode == 'all':
        for t in tabs:
            print("%s \t %s \t %s" %(t.URL(), t.title(), t.id()))

if __name__ == "__main__":
    main(sys.argv)
