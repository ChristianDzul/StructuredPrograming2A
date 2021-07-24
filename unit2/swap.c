#include <stdio.h>
#include "/mnt/c/Users/manan/StructuredPrograming2A/unit2/folderTest/utils.h"
#include <stdlib.h>

int a = 10;
int b = 20;

int main( ){
    printf("Num1:%d , Num2: %d\n", a, b);
    int*New1 = &a;
    int*New2 = &b;
    printf("Swapping numbers...\n");
    SwapVariables (&a, &b);
    printf ("Swapped values:\n");
    printf ("Num1=%d , Num2: %d\n", a, b);
    return 0;
}

