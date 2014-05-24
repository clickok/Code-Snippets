#!/usr/bin/python3
""" Test the output of the tile coding software
	
	It takes input via files specified in the command line arguments:

		$ python test_tiles_output.py <input_file> <output_file> 

	* CURRENTLY DOESN'T DO ANYTHING WITH THE INPUT FILE! *

	## The input file is formatted as follows:

	The first line will be of the form: 
		4 512 <num_floats> <num_ints>

	Each line after the first has a total of <num_floats> + <num_ints> entries.
	
	The first <num_floats> entries will be floating point numbers, distributed
	uniformly between 0 and 1, multiplied by <float_factor>, and then offset
	by <float_offset>.

	The remaining <num_ints> entries will be integers sampled uniformly between
	<int_min> and <int_max>


	## The output file is formatted as follows:
	
	The first line being the same as in the input file (passed to 
	"tile_test.cc", say). That is:

	<num_tilings> <memory_size> <num_floats> <num_ints>

	The following lines are all of the form:

	<d_1> <d_2> ... <d_N>

	Where "d" denotes a digit, and N = <num_tilings> 
"""

import numpy as np
import os
import sys

def main():
	if len(sys.argv) < 3:
		print("You need to specify two files to be read, <input> and <output>")
		exit()

	input_path  = sys.argv[1].strip()
	output_path = sys.argv[2].strip()

	if not(os.path.isfile(input_path)):
		print("You need to specify an input file")
		exit()
	elif not(os.path.isfile(output_path)):
		print("You need to specify an output file")
		exit()

	try:
		input_file  = open(input_path,  "r")
		output_file = open(output_path, "r")

		# Get output file's information from first line
		line = output_file.readline()
		lst = [int(i) for i in line.strip().split()]
		num_tilings, memory_size, num_floats, num_ints = lst

		tile_count = np.zeros(memory_size)


		for line in output_file:
			lst = [int(i) for i in line.strip().split()]
			print(lst)
			tile_count[lst] += 1

		print(tile_count)
			
	
	finally:
		input_file.close()
		output_file.close()

if __name__ == "__main__":
	main()