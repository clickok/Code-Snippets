#!/usr/bin/python3

""" Generate some test input for tile coding. 

	Not perfect, but easy enough to work with. See "tile_test.cc" and the 
	README for more information.

	From command line, it takes arguments of the form:
	<num_lines> <num_floats> <float_factor> <float_offset> <num_ints> <int_min> <int_max>

	With types:
	<int> <int> <float> <float> <int> <int> <int>

	The above is unwieldy, and this makes me sad, but in practice it should 
	generate output (to stdout) of length "num_lines", for use with  with 
	"tile_test.cc". Note that, as the programs are currently, you may want
	to modify the output's default values for <num_tilings> and <memory_size>

	The first line will be of the form: 
		4 512 <num_floats> <num_ints>

	Each line after the first has a total of <num_floats> + <num_ints> entries.
	
	The first <num_floats> entries will be floating point numbers, distributed
	uniformly between 0 and 1, multiplied by <float_factor>, and then offset
	by <float_offset>.

	The remaining <num_ints> entries will be integers sampled uniformly between
	<int_min> and <int_max>

	Example:
	
	$ python test_input_generator.py 10 2 4.0 7.2 1 0 5

	Would generate a file of 11 lines, the first line as specified, and the 
	next ten lines containing two floats in [7.2, 11.2) and one int in [0, 5] 
"""

import random
import sys

# Fancy way of parsing the arguments
funcLst = [int, int, float, float, int, int, int]

def parseArgs(argLst):
	ret = []
	for i in range(len(argLst)):
		#print(funcLst[i](argLst[i]))
		ret.append(funcLst[i](argLst[i]))

	return ret 

	



def main():
	if len(sys.argv) == 1:
		raise RuntimeError("You need to specify eight (8) arguments")
	
	elif sys.argv[1] in {"help", "--help", "-h"}:
		print(__doc__)
	
	elif len(sys.argv) != 8:
		raise RuntimeError("You need to specify eight (8) arguments")

	else:
		arg_vals = parseArgs(sys.argv[1:])

	# Horrible, horrible unpacking
	num_lines, num_floats, float_factor, float_offset, num_ints, int_min, int_max = arg_vals

	# Print the header
	print("4 512", num_floats, num_ints, end=" ")

	for line in range(num_lines):
		for i in range(num_floats):
			print("{:f}".format(random.random()*float_factor + float_offset), end=" ")

		for i in range(num_ints):
			print(random.randint(int_min, int_max), end=" ")

		print()




if __name__ == "__main__":
	main()