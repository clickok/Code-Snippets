"""
Implementation of a dictionary which only accepts N-D coordinate tuples.
"""

from collections import defaultdict


class DiscreteCoordDict(defaultdict):
	def __init__(self, ndim, default_factory=None):
		assert(isinstance(ndim, int))
		self.__dict__['ndim'] = ndim
		super().__init__(default_factory)

	def __setattr__(self, name, value):
		if name is not 'ndim':
			self.__dict__[name] = value
		else:
			raise AttributeError('Immutable attribute:', name)

	def __setitem__(self, key, value):
		if not isinstance(key, tuple):
			raise KeyError("Invalid key: keys must be tuples.")
		elif len(key) != self.ndim:
			raise KeyError("Invalid key: keys must be of length", self.ndim)
		elif not all(isinstance(x, int) for x in key):
			raise KeyError("Invalid key: keys must be integer-valued.")
		else:
			super().__setitem__(key, value)

	def __delattr__(self, name):
		if name is not ndim:
			del self.__dict__[name]
		else:
			raise AttributeError('Immutable attribute:', name)