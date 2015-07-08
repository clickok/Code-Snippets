#!python3
"""
A quick script to list all open tabs for Google Chrome, along with their URL.

Also included are some functions that may be reusable in component form.
"""

import appscript as app
import sys

def get_windows():
	"""List all open Chrome windows as a list of Applescript objects"""
	return app.app('Google Chrome').windows()

def get_all_tabs(win_ids=None):
	"""Return a list of all Chrome tabs, OR those with the specified window IDs"""
	if win_ids:
		windows = [w for w in get_windows() if w.id() in win_ids]
	else:
		windows = get_windows()

	return [t for t in w.tabs() for w in windows]

def print_windows():
    """ Print the window titles and ids, for convenience """
    C = app.app('Google Chrome')
    if C.windows.count():
        for w in C.windows():
            print(w.id(), '\t', w.title()[:min(70, len(w.title()))])

def print_all_tabs(win_ids=None):
	"""List all tabs by ID, then title <TAB> URL on the next line"""
	if win_ids:
		windows = [w for w in get_windows() if w.id() in win_ids]
	else:
		windows = get_windows()
	
	for w in windows:
		tabs = w.tabs()
		for t in tabs:
			print(t)
			print(t.title(), "\t", t.URL())

if __name__ == "__main__":
	if len(sys.argv) > 1:
		win_ids = [int(x) for x in sys.argv[1:]]
		print_all_tabs(win_ids)
	else:
		print_windows()
