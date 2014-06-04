#!/python3
""" 
Find and isolate LEDs (or other sufficiently bright lights) in a series of PNG 
images for use in other scripts.

For example, we seek to find the LEDs of a robot to be composited in 
order to draw its path, if we have a series of PNGs corresponding to frames in
a movie of the robot moving around.

1. 	Apply "-black-threshold" to images
2. 	Convert black regions to transparent 

Usage:
	python isolate_leds.py INPUT_DIR OUTPUT_DIR
"""

import os
import os.path
import sys
import subprocess


def main():
	# For debugging
	MONITOR = True
	if MONITOR:
		IF_MON = "-monitor"
	else:
		IF_MON = ""

	# Variables affecting image processing 
	THRESHOLD = "50%"

	# Make sure that 
	try:
		INPUT_DIR  = os.path.abspath(sys.argv[1])
		OUTPUT_DIR = os.path.abspath(sys.argv[2])
		assert(os.path.isdir(INPUT_DIR))
		if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
	
	except AssertionError as e:
		print("\nERROR: Input directory was not a valid directory\n")
		raise e

	except Exception as e:
		raise e 

	print("Operating on images in:", INPUT_DIR, "saving results in", OUTPUT_DIR)

	# Convert Red and Green pixels below threshold to black following:
	# `$ mogrify -channel Red,Green -black-threshold 50% OUTPUT_DIR/*.png`
	print("Converting pixels below threshold to black")
	subprocess.call(["mogrify", IF_MON, "-path", OUTPUT_DIR, "-channel", "Red,Green", 
									 "-black-threshold", THRESHOLD, INPUT_DIR+"/*.png"])

	# Convert black regions to transparent following:
	# `$ mogrify -fuzz 5% -transparent black OUTPUT_DIR/*.png`
	print("Converting black regions to transparent")
	subprocess.call(["mogrify", IF_MON, "-transparent", "black", OUTPUT_DIR+"/*.png"])


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print(__doc__)
		exit()
	main()