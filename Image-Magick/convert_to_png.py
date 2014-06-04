#!/python3
"""
Convert all images from some directory to png, output the resulting images
in another (potentially)

Usage:
	python convert_to_png.py INPUT_DIR OUTPUT_DIR
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

	print("Converting images from:", INPUT_DIR, "to PNGs in", OUTPUT_DIR)

	# Convert JPEGs to PNG via
	# `$ mogrify -format png *.jpg`
	print("Converting images from JPEG to PNG")
	subprocess.call(["mogrify", IF_MON, "-path", OUTPUT_DIR, "-format", "png", INPUT_DIR+"/*.jpg"])

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print(__doc__)
		exit()
	main()