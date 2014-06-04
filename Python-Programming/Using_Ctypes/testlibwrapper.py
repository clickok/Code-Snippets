import ctypes
import os


testlib = ctypes.CDLL("./testlib.so")
testlib.myprint()