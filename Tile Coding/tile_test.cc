/* 	tile_test.cc 
	For testing the tile coding software. 
	Written in C but compiled w/ C++ for compatibility,

	The program gets input via stdin, so either typing or IO redirection works.
	First line of the input must be of the form:

	<num_tilings> <memory_size> <num_floats> <num_ints>

	Subsequent lines must be of the form:

	<f_1> <f_2> ... <f_N> <d_1> <d_2> ... <d_M>

	Where "f" and "d" denote floats and integers respectively, and N and M are
	equal to <num_floats> and <num_ints>, also respectively.

	The output will contain the tilings of the values passed to the program.
	So, if there were "L" lines (excluding the one that specified the number
	of tilings and such), there would be "L" lines of output. 

	The output lines will be of the form:

	<d_1> <d_2> ... <d_T>

	Where "T" is equal to <num_tilings>

	*************************************************************************** 
	I've checked this and it seems to be running properly, so some debug 
	statements have been removed. The file "tile_test2.c" contains the code
	with debug statements, although I believe it to be only a few changes
	behind this one, if it is behind at all.

	There are some subtle bugs when parsing input like this.
	Using "getline" or "fgets" to grab a single line before we try to
	parse the potentially varied number of entries requires us to either build
	a format string on the fly, or use some sort of looping strategy.

	I used looping here, but the danger is that in so doing you need to
	increment the point (that tells you where you are in the line) in order to
	get the next entry, and C will allow you to *keep* incrementing this until
	you smash the stack and segfault. Further, getline() acts as an accomplice,
	because it keeps reallocating when you don't have any space, and there's
	not really a way to check for boundaries or type safety! Also, since it's
	the only thing being allocated at that stage of the program, the 
	difficulties compound. The realization of how that all came together was
	fun, even if it's not an experience I wish to repeat. 
*/

#include <stdio.h>
#include <stdlib.h>

#include "tiles2.hh"

//#define NDEBUG

/* Zed Shaw's debug macros */
#ifndef __dbg_h__
#define __dbg_h__

#include <stdio.h>
#include <errno.h>
#include <string.h>

#ifdef NDEBUG
#define debug(M, ...)
#else
#define debug(M, ...) fprintf(stderr, "DEBUG %s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#endif

#define clean_errno() (errno == 0 ? "None" : strerror(errno))

#define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%d: errno: %s) " M "\n", __FILE__, __LINE__, clean_errno(), ##__VA_ARGS__)

#define log_warn(M, ...) fprintf(stderr, "[WARN] (%s:%d: errno: %s) " M "\n", __FILE__, __LINE__, clean_errno(), ##__VA_ARGS__)

#define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%d) " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)

#define check(A, M, ...) if(!(A)) { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

#define sentinel(M, ...)  { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

#define check_mem(A) check((A), "Out of memory.")

#define check_debug(A, M, ...) if(!(A)) { debug(M, ##__VA_ARGS__); errno=0; goto error; }

#endif

#define LINE_MAX 1024

int main(int argc, char * argv[])
{
	/* Variables for reading in the input */
	int i;
	int offset;
	char * 	line 		= NULL;
	size_t 	len 		= 0;
	ssize_t read; 

	/* Variables for parsing single lines */
	int tmp_int; 
	int tmp_read;
	int total_offset=0;
	float tmp_float;
	int line_count=0;

	/* For calling tiles() with */
	int num_tilings, memory_size, num_floats, num_ints;
	float *float_array;
	int *int_array;  
	int *tile_array;

	/* Get the first line */ 
	line = (char *) malloc(LINE_MAX);
	if ((read = getline(&line, &len, stdin)) != -1)
	{
		tmp_read = sscanf(line, "%d %d %d %d", &num_tilings, &memory_size, &num_floats, &num_ints);
		debug("Read: \t%s", line);
		debug("Separate entries in line: %d", tmp_read);
		debug("num_tilings: %d, memory_size: %d, num_floats: %d, num_ints: %d", 
			   num_tilings, memory_size, num_floats, num_ints);
		printf("%d %d %d %d\n", num_tilings, memory_size, num_floats, num_ints);
	}
	
	/* Initialize arrays based on input's first line*/
	float_array = (float *) malloc((num_floats + 1) * sizeof(float));
	int_array   = (int *) 	malloc((num_ints + 1) * sizeof(int));
	tile_array	= (int *)	malloc((num_tilings + 1) * sizeof(int));


	while ((read = getline(&line, &len, stdin)) != -1) 
	{
		line_count++;
		offset = 0;
		total_offset = 0;
		debug("Line #: %d, pointer: %ld", line_count, (long int) line);
		
		/* Read the floats */ 
		for (i=0; i < num_floats; i++)
		{
			tmp_read = sscanf(line + total_offset, "%f%n", &tmp_float, &offset);
			if (tmp_read != 1) debug("Possible error reading line %d", line_count);
			
			float_array[i] = tmp_float;
			total_offset += offset;
		}
		/* Parse the ints */ 
		for (i=0; i < num_ints; i++)
		{
			tmp_read = sscanf(line, "%d%n", &tmp_int, &offset);
			if (tmp_read != 1) debug("Possible error reading line %d", line_count);

			int_array[i] = tmp_int;
			total_offset += offset;
		}

		/* Perform tiling, get the resulting output */
		tiles(tile_array, num_tilings, memory_size, float_array, num_floats, int_array, num_ints);
		for (i=0; i < num_tilings; i++)
		{
			printf("%d ", tile_array[i]);
		}
		printf("\n");

	}
	debug("REACHED END OF FILE\n");

	// Should free memory?
	exit(EXIT_SUCCESS);
}