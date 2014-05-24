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

*/

#include <stdio.h>
#include <stdlib.h>

#include "tiles.hh"

#define LINE_MAX 1024

int main(int argc, char * argv[])
{
	/* Variables for reading in the input */
	int i;
	int count;
	int offset;
	char * 	line 		= NULL;
	char * 	format_str	= NULL;
	size_t 	len 		= 0;
	ssize_t read; 

	/* For calling tiles() with */
	int num_tilings, memory_size, num_floats, num_ints;
	float *float_array;
	int *int_array;  

	/* Initialize the formatted variable */
	format_str = (char *) malloc(LINE_MAX * sizeof(char));

	if ((read = getline(&line, &len, stdin)) != -1)
	{
		count = sscanf(line, "%d %d %d %d", &num_tilings, &memory_size, &num_floats, &num_ints);
		printf("Read: \t%s", line);
		printf("Parsed: %d %d %d %d\n", num_tilings, memory_size, num_floats, num_ints);
		printf("Count: %d\n", count);
	}
	/* Create the format string */

	
	/* Initialize arrays for storing values from line */
	float_array = (float *) malloc(num_floats * sizeof(float));
	int_array   = (int *) 	malloc(num_ints * sizeof(int));

	while((read = getline(&line, &len, stdin)) != -1)
	{
		offset = 0;
		for(i=0; i < num_floats; i++)
		{
			if (1 != sscanf(line, "%f%n", &float_array[i], &offset))
			{
				fprintf(stderr, "\n[ERROR]: Failed to read line: %s", line);
				fprintf(stderr, "[ERROR]: Previous part: %s", line - offset);
				fprintf(stderr, "Value: %f\n", float_array[i]);
				exit(EXIT_FAILURE);
			}
			line += offset;
			printf("%f ", float_array[i]);
		}

		for(i=0; i < num_ints; i++)
		{
			if (1 != sscanf(line, "%d%n ", &int_array[i], &offset))
			{
				fprintf(stderr, "[ERROR]: Failed to read line: %s", line);
				exit(EXIT_FAILURE);
			}
			line += offset;
			printf("%d ", int_array[i]);
		}
		printf("\n\n");
	}
	if (line)
	{
		free(line);
	}
	free(float_array);
	free(int_array);
	exit(EXIT_SUCCESS);
}