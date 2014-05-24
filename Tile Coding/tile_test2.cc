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

	... This was surprisingly torturous because of strange bugs encounted with
	the input processing; I am still not sure if I've found all of them, but
	it seems to run, now.

*/

#include <stdio.h>
#include <stdlib.h>

#include "tiles2.hh"

#define NDEBUG

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
	int count;
	int offset;
	char * 	line 		= NULL;
	char *  old_line	= NULL;
	size_t 	len 		= 0;
	ssize_t read; 

	/* For calling tiles() with */
	int num_tilings, memory_size, num_floats, num_ints;
	float *float_array;
	int *int_array;  
	int *tile_array;

	/* Get the first line */ 
	line = (char *) malloc(LINE_MAX);
	if ((read = getline(&line, &len, stdin)) != -1)
	{
		count = sscanf(line, "%d %d %d %d", &num_tilings, &memory_size, &num_floats, &num_ints);
		debug("Read: \t%s", line);
		debug("Count: %d", count);
		printf("%d %d %d %d\n", num_tilings, memory_size, num_floats, num_ints);
	}
	
	/* Initialize arrays based on input's first line*/
	float_array = (float *) malloc((num_floats + 1) * sizeof(float));
	int_array   = (int *) 	malloc((num_ints + 1) * sizeof(int));
	tile_array	= (int *)	malloc((num_tilings + 1) * sizeof(int));



	int tmp_int, tmp_read;
	int total_offset=0;
	float tmp_float;
	int line_count=0;
	//while ((read = getline(&line, &len, stdin)) != -1) 
	while(fgets(line, LINE_MAX, stdin) != NULL)
	{
		line_count++;
		offset = 0;
		total_offset = 0;
		debug("Read line: %d", line_count);
		debug("Length: %zu", len);
		debug("Line Ptr: %ld Old Ptr: %ld", (long int) line, (long int) old_line);
		debug("Line: %s", line);
		for (i=0; i < num_floats; i++)
		{
			tmp_read = sscanf(line + total_offset, "%f%n", &tmp_float, &offset);
			float_array[i] = tmp_float;
			total_offset += offset;
			debug("i: %d, tmp_read: %d, tmp_float: %f", i, tmp_read, tmp_float);
		}
		for (i=0; i < num_ints; i++)
		{
			tmp_read = sscanf(line, "%d%n", &tmp_int, &offset);	
			int_array[i] = tmp_int;
			total_offset += offset;
			debug("i: %d, tmp_read: %d, tmp_int: %d", i, tmp_read, tmp_int);
		}

		/* Perform tiling, get the resulting output */
		debug("About to tile...");
		tiles(tile_array, num_tilings, memory_size, float_array, num_floats, int_array, num_ints);
		debug("About to print...");
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