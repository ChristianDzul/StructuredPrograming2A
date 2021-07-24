#include <stdio.h>
#include<stdlib.h>

float add=0;
float Var=0;
float result=0;
int numbers;


int main (int argc, char* argv[]){
    printf("HELLO!!!\n");
    printf("Starting Program...\n");
    printf( "Calculating the numbers entered.\n");
    for (numbers = 1; numbers < argc; numbers++){ 
        Var = atof(argv[numbers]);
        add+=Var;
        result=(add)/numbers;
    if (numbers== (argc-1)){
    printf("Average Value:%f\n", result);  
    }
    }
    return 0;
}  
