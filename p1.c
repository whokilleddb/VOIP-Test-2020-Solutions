#include <stdio.h>
#include <stdlib.h>
void main()
{
	int i,j;
	for (i=65;i<70;i++) //Getting Rows
	{
		for(j=65;j<=i;j++) // Getting Columns
		{
			printf("%c",i);	// Printing Same Character Along The Row 
		}
	printf("\n");
	}
}

/*
Compilation Command : 
gcc Q1.c -o Q1.out 

Output :
A
BB
CCC
DDDD
EEEEE

*/