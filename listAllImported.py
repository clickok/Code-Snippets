""" 
Print all of the functions in some module, AND THOSE IT LOADS!

Doesn't quite work because some of those objects are obscured and I 
don't want to spend forever just because this is neat.

Usage: 
	python listAllImported.py <path_to_target>
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
	# Keep a set of the modules we imported beforehand
	prev_imports = set(sys.modules)
	# Import it, using the __import__ function 
	target_module = __import__(target_name) 

	print("Imported:", target_module.__name__)
	try:
		print("From file:", target_module.__file__)
	except Exception as e:
		pass 

	# Get which modules are newly imported as a result
	new_imports = list(set(sys.modules) - prev_imports)
	print("Newly imported modules:", new_imports)

	# Get a list of the functions in the target module, and print it
	# An awesome list comprehension
	functions_list = [x for m in new_imports for x in inspect.getmembers(sys.modules[m]) if inspect.isfunction(x[1])]

	# OK, we can also do it like this:
	module_list = [sys.modules[m] for m in new_imports]
	mod_members = [x for m in module_list for x in inspect.getmembers(m)]
	functions_list = [x for x in mod_members if inspect.isfunction(x[1])] 
	for i in functions_list:
		print(i[0])