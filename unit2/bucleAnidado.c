#include <stdio.h>
#include <stdlib.h> //atoi, atof
#include <stdbool.h>

#define TAN 10

int list[TAN] = {105,20,21,40,33,60,70,50,93,100};
int idx = 0 ;

typedef int INTEGER;

int main( int argc, char** argv ){
        int index2 = 0;
        for (int index = 0; index < TAN; index++, index2++){   ///for principal
            printf( "index: %d, value: %d.\n\a", index, list[index]);
            for (size_t i = 0; i < 3; i++){ //bucle anidado o for anidado
                printf("HolaMundo!!!\n");
            }
        }
        return 0;
}