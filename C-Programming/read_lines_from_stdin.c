/* 
	Reads lines from stdin, determines their length and prints them to stdout.

	It keeps reading until it reaches the end of file.
*/

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[])
{
	char * 	line = NULL; 
	size_t 	len 	= 0;
	ssize_t read; 
	while((read = getline(&line, &len, stdin)) != -1)
	{
		printf("Retrieved line of length %zu :\n", read);
		printf("%s", line);
	}
	if (line)
	{
		free(line);
	}
	exit(EXIT_SUCCESS);
	return 0;
}