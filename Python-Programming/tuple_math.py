"""
Routines for doing math with tuples.
"""
import operator
from numbers import Number 


# Example use of map and operator methods
def tuple_add(a, b):
    return tuple(map(operator.add, a, b))

def tuple_div(a, b):
    return tuple(map(operator.truediv, a, b))

def tuple_mul(a, b):
    return tuple(map(operator.mul, a, b))

def tuple_sub(a, b):
    return tuple(map(operator.sub, a, b))


class Vector(tuple):
    def __abs__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__abs__(x, other), self))
        else:
            return Vector(map(operator.__abs__, self, other))
    
    def __add__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__add__(x, other), self))
        else:
            return Vector(map(operator.__add__, self, other))
    
    def __and__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__and__(x, other), self))
        else:
            return Vector(map(operator.__and__, self, other))
    
    def __floordiv__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__floordiv__(x, other), self))
        else:
            return Vector(map(operator.__floordiv__, self, other))
    
    def __inv__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__inv__(x, other), self))
        else:
            return Vector(map(operator.__inv__, self, other))
    
    def __lshift__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__lshift__(x, other), self))
        else:
            return Vector(map(operator.__lshift__, self, other))
    
    def __mul__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__mul__(x, other), self))
        else:
            return Vector(map(operator.__mul__, self, other))
    
    def __neg__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__neg__(x, other), self))
        else:
            return Vector(map(operator.__neg__, self, other))
    
    def __or__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__or__(x, other), self))
        else:
            return Vector(map(operator.__or__, self, other))
    
    def __pos__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__pos__(x, other), self))
        else:
            return Vector(map(operator.__pos__, self, other))
    
    def __rshift__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__rshift__(x, other), self))
        else:
            return Vector(map(operator.__rshift__, self, other))
    
    def __sub__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__sub__(x, other), self))
        else:
            return Vector(map(operator.__sub__, self, other))
    
    def __truediv__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__truediv__(x, other), self))
        else:
            return Vector(map(operator.__truediv__, self, other))
    
    def __xor__(self, other):
        if isinstance(other, Number) or len(other) == 1:
            return Vector(map(lambda x: operator.__xor__(x, other), self))
        else:
            return Vector(map(operator.__xor__, self, other))