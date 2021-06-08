#include <stdio.h>
#include <stdlib.h> //atoi, atof
#include <stdbool.h>



#define TAN 10

int lista[TAN] = {10,20,30,40,50,60,70,80,90,100};
int idx = 0;

int main(int argc, char** argv){

    int index2 = 0;
    for(int index = 1; index <= TAN; index++, index2++){

        printf("index: %d, value: %d. \n\a", index, lista[index]);
    }

    while (true){
        if(lista[idx == 50]){
            break }
        idx++
         }
    printf("idx found: %d", idx);

    int idx_for = 0;
    for ( ; lista[idx_for] != 50; idx_for++){
        
        printf("idx_for found: %d", idx_for);
    }
    return 0;
}