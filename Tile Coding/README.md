# Tile Coding

There are a couple of different implementations that Rich has made available at various RLAI sites, such as [rlai.net](http://rlai.net), [Rich's site](http://incompleteideas.com), and probably elsewhere as well. 

Here, I've made some slight modifications (such as changing the extensions, because they programs are really C++ files) and added a Makefile. There are different versions, and I am not positive that I have the most up-to-date files here. The older code ("tiles.c") is simpler, but has less functionality.

The reference manual is available at [Rich's site](http://incompleteideas.net/rlai.cs.ualberta.ca/RLAI/RLtoolkit/tiles.html)

## Changes

* Modified extensions to reflect that they are C++ files

* Added a variable to "tiles.cc", "bb_i", which is used for iteration but caused complaints from the compiler because it was compared to a size_t type (which is an unsigned int, not an int)

* Changed the includes;
	* Use <math.h> instead of "math.h"
	* Changed the "IFNDEF" stuff to reflect that there are different .hh files
	* Change the files to include their respective .hh files  