# Simple Makefile
#
# So we're making files in c++ now!
# Author: BB
# --------------------------------------------------

CC      =  g++
CFLAGS  = -I. -Wall
CLIBS   = -lm 
LDFLAGS = 
LDLIBS  = 

# Project Specific
SOURCES = tile_test.cc tiles.cc tiles2.cc
DEPS    = tiles.hh tiles2.hh
OBJECTS = $(subst .cc,.o, $(SOURCES))

EXECS  =  tile_test tile_test2

all: $(EXECS)
	

tile_test: $(OBJECTS)
	$(CC) $(LDFLAGS) -o $@ $(OBJECTS) $(LDLIBS)

%.o: %.cc $(DEPS)
	$(CC) $(CFLAGS) $(CLIBS) -c -o $@ $< 

.PHONY: clean

clean:
	rm -f $(EXECS)

.PHONY: echo_vars

echo_vars:
	@echo "SOURCES: $(SOURCES)"
	@echo "DEPS: $(DEPS)"
	@echo "OBJECTS: $(OBJECTS)"
	@echo "EXECS: $(EXECS)"
