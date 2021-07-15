#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./folderTest/utils.h"



int myInt = 4;
float myFloat = 3.1416;

int * pointerInt = &myInt;

int main(){
        
        printf("addres myInt: %p,   myInt: %d  \n",  &myInt , myInt  );
        printf("addres myFloat: %p,  myFloat: %f  \n",  &myFloat , myFloat  );
        printf("address pointerInt: %p, pointerInt: %p\n", &pointerInt,   pointerInt  );
        *pointerInt = 6;
        printf("addres myInt: %p,   myInt: %d  \n",  &myInt , myInt  );


        // Array myArray;
        Array* myArray =    returnArray();
        printf(  "%d\n", myArray->dirArray[1]  ); // -> sirve para acceder a un alojamiento creado por malloc que engloba a la estructurra de tipo array, esto te permite acceder a cosas muy internas, como si de ficheros se tratase
        
        // malloc(), realloc, calloc();
        

        return 0;
}