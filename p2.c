#include <stdio.h>
#include <stdlib.h>
int main(int argc , char *argv[])
{
	if (argc > 1) // Checking For Command line Arguments
	{
		int c; 
		double x;
		x=atof(argv[1]); //Convert char into float 
		c=(int)(x*1000)%10; //Get The Thousandth Character
		if (c==0) // Checking If The Last Character Is Zero
		{
			printf("%.2f",x);
			return 0;
		}
		else
		{
			if(c<5) // the Given Problem requires rounding off to the next hundredth place or else Case fails
			{
				x=x+0.005;
				printf("%.2f",x);
				return 1;
			}
			else
			{
				printf("%.2f",x);
				return 2;				
			}
		}
	}
	else
	{
		return -1;
	}
}


/*
Compilation Command :
gcc Q2.c -o Q2.out

Output :
./Q2.out 2.210
2.21 

./Q2.out 5.712                                        
5.72  

./Q2.out 9.268                                 
9.27 

*/





