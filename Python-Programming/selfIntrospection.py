""" 
An example of self-introspection; uses inspect and sys to list all of the
functions in the current module (i.e., this file)
"""
import inspect
import sys

def foo():
	print("foo")

if __name__ == "__main__":
	current_module = sys.modules[__name__]
	functions_list = [x for x in inspect.getmembers(current_module) if inspect.isfunction(x[1])]
	for i in functions_list:
		print(i)