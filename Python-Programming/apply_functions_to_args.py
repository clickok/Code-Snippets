#!/usr/bin/python3

""" Applies a list of functions to command line arguments. 

	For quick-and-dirty command line argument handling.
"""

import sys

# List of functions to apply
funcLst = [int, int, float, float, int, int, int]

def parseArgs(argLst):
	for i in range(len(argLst)):
		print(funcLst[i](argLst[i]))


def main():
	if sys.argv[1] in {"help", "--help", "-h"}:
		print(__doc__)
	else:
		parseArgs(sys.argv[1:])


if __name__ == "__main__":
	main()