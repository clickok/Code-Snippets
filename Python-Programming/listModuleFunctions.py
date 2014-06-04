""" 
Print all of the functions in some module

Usage: 
	python listModuleFunctions.py <path_to_target>
"""
import inspect
import os, os.path 
import sys

def foo():
	print("foo")

if __name__ == "__main__":
	# First, get the path to the file to be imported, and additional information
	try:
		target_path = os.path.abspath(sys.argv[1].strip())
		target_dir  = os.path.dirname(target_path)
		target_name = os.path.splitext(os.path.basename(target_path))[0]
	except IndexError as e:
		print("Index Error!")
		print("Need to specify a target module's path")
		exit()

	# Add the target's directory to the system's path, so import can find it
	sys.path.append(target_dir)
	# Import it, using the __import__ function 
	target_module = __import__(target_name) 

	print("Imported:", target_module.__name__)
	try:
		print("From file:", target_module.__file__)
	except Exception as e:
		pass 

	# Get a list of the functions in the target module, and print it
	functions_list = [x for x in inspect.getmembers(target_module) if inspect.isfunction(x[1])]
	for i in functions_list:
		print(i)
