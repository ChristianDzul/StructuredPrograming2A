#include <stdio.h>
#include <stdlib.h> //aoit, atof//
#include <string.h>  //strcpy//

int my_int = 0; // %i o %d
float my_float = 3.14; // %f //en verdad era 0
char my_char = 'c'; // %c
char my_str[10] = "0"; //%s

float second_float = 0.0;
//Pointer//
int* my_ptr_int = &my_int; // %p

int main( int argc, char** argv){
    //pegando el argv a la variable string//
    strcpy(my_str, argv[1]);
    //convertir string a entero//
    int base = atoi ( my_str);

    strcpy(my_str, argv[2]);
    int altura = atoi( my_str);

    printf("my_int: %i, my_float: %f, my char: %c, my_str: %s, my_ptr_int: %p", my_int, my_float, my_char, my_str, my_ptr_int);
    printf("argc: %i, element1: %d, elem2 : %s, char: %c  \n", argc, base * altura, argv[2], 'L' );

    return 0;
}