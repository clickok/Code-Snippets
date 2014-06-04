#!/python3
"""
Given a directory full of images (which are, by assumption, PNGs) compute the
median pixel value for each pixel, and create an image composed of these pixels.

This should hopefully give an image where transient objects in some scene are
removed, e.g. get rid of traffic in images of a busy street

Usage:
	python compute_background.py INPUT_DIR OUTPUT_PATH

Example: 
	python compute_background.py ./Original-Images still_image.png  

"""

import os
import sys
import subprocess

def main():
	# For debugging
	MONITOR = True
	if MONITOR:
		IF_MON = "-monitor"
	else:
		IF_MON = ""

	try:
		INPUT_DIR 	= os.path.abspath(sys.argv[1])
		OUTPUT_PATH	= os.path.abspath(sys.argv[2])
		assert(os.path.isdir(INPUT_DIR))
		
		# Ensure that we are making the output file a PNG
		OUT_SPLITEXT = os.path.splitext(OUTPUT_PATH)
		if OUT_SPLITEXT[1] != ".png":
			OUTPUT_PATH = os.path.join(OUT_SPLITEXT[0], ".png")

	except AssertionError as e:
		print("\nERROR: Input directory was not a valid directory")
		raise e

	except Exception as e:
		raise e

	print("Computing median for images in:", INPUT_DIR, "saving result at", OUTPUT_PATH)

	# Convert JPEGs to PNG via
	# `$ convert -evaluate-sequence Median INPUT_DIR/*.png OUTPUT_PATH`
	print("Computing median of images...")
	subprocess.call(["convert", IF_MON, "-evaluate-sequence", "Median", 
									 INPUT_DIR+"/*.png", OUTPUT_PATH])

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print(__doc__)
		exit()
	main()