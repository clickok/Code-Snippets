#python3
""" A bunch of scrolling unicode to look like a cheap knockoff of the so-called
'Digital Rain' in The Matrix
"""

import numpy as np
import random
import time

def main():
	math_chars = ["؈", "⅀", "⅁", "⅋", "∀", "∅", "∄", "∉", "∈", "∐","∢", "≑",
	"⋉", "⟱", "⨊", "⨷", "⩤", "⫷", "⫸", "𝛁"]
	currency_chars = ["$", "£", "¥", "૱", "₡", "₤", "₱", "₹", "₴", "￦", "₳",
	"₮", "₭"]
	misc_chars = ["℥", "℧", "⅏", "♥", "♣", "✠", "✡", "⼳", "⼤", "⼣", "⼢", "⼦",
	"⼫", "⽁", "⽃", "⽒", "⽘", "⽤", "⽢"]

	combined = math_chars + currency_chars + misc_chars
	line_length = 80
	line = np.random.choice(combined, size=[line_length])
	show = np.random.choice([0, 1], size=(line_length,), p=[0.3, 0.7])
	while True:
		for i in range(line_length):
			if show[i] != 0:
				print(line[i], end="")
			else:
				print(" ", end="")
	
		if random.random() < 0.3:
			line = np.random.permutation(line)
			print("\r", end="")
		else:
			line = np.random.choice(combined, size=[line_length])
			print("", end="")
		show = np.random.choice([0, 1], size=(line_length,), p=[0.2, 0.8])
		time.sleep(random.random()*0.2)

if __name__ == "__main__":
	main()