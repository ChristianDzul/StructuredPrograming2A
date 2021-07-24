#include <stdio.h>

int AgeValidation (int *Age){
    scanf("%d",Age); 
        if (*Age < 18)
        {
            printf("Warning: You nead at leats 18 years old to acces to the program\n");
        }

        else
        {
            printf("WELCOME!!!\n");
        }
    return 0;
}

int main(){
    printf("Initializing Program...\n");
    printf("Enter your age:\n");
    int Age [100];
    AgeValidation(Age);
    return 0;
}