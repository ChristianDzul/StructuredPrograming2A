#include <stdio.h>
#include <stdlib.h>


int number;

int CheckNumber (int number){
    for (number = 1; number <= 100; number++)
    {
        if (number%3 == 0 && number%5 == 0)
        {
            printf("%d\n", number);
        }
        
    } 
    return 0;  
}


int main(int argc, char** argv){
    printf ("Initializing Program Calculator...\n");
    printf("These are the values of the numbers divisible by 3 and 5:\n");
    CheckNumber(number);
return 0;
}
