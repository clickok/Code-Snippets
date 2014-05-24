
#include <stdio.h>
#include <stdlib.h>

#include "tiles2.hh"

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

	num_floats = 2;
	num_ints   = 1;

	/* Initialize arrays for storing values from line */
	float_array = (float *) malloc((num_floats+1) * sizeof(float));
	int_array   = (int *) 	malloc((num_ints +1)* sizeof(int));

	while((read = getline(&line, &len, stdin)) != -1)
	{
		offset = 0;
		printf("%s", line+offset);
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
	return 0;
}