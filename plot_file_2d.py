#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def plot_2d_scatter(x_data, y_data):
	fig, ax = plt.subplots(1)
	ax.scatter(x_data, y_data)
	plt.show()


def main():
	pass

if __name__ == "__main__":
	main()