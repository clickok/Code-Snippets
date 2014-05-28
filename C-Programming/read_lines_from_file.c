/* 	read_lines_from_file.c 
	Reads lines from a file (currently "/etc/motd"), determines their length 
	and prints them to stdout.

	It keeps reading until it reaches the end of file.
*/

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

#define LINE_MAX 1024

int main(int argc, char * argv[])
{
	FILE * fp;
	char * 	line = NULL; 
	size_t 	len 	= 0;
	ssize_t read;

	/* Open the file in read mode */
	fp = fopen("/etc/motd", "r");

	line = (char *) malloc(LINE_MAX * sizeof(char));

	/* Iterate through it, until something stops you */
	while((read = getline(&line, &len, stdin)) != -1)
	{
		printf("Retrieved line of length %zu :\n", read);
		printf("%s", line);
	}

	/* Free any memory still in use */
	if (line)
	{
		free(line);
	}
	exit(EXIT_SUCCESS);
	return 0;
}