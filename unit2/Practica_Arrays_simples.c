#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Creando un array, primer paso//

int myIntArray[5]; //se pueden llenar de datos o no.

//defincion y declaración de funciones///

void fillArray(int array[], size_t tamano){ //ira llenando el array hasta donde se ropa la condicion donde "i" es menor a tamaño que es 5
    for (size_t i = 0; i < tamano; i++)
    {
        array[i] = i*2; //aqui estamos seteando que i siempre sera 1
    }
    return;
};

void printArray1D(int array[], size_t tamano){  //para imprimir los valores ingresador al array
    for (size_t i = 0; i < tamano; i++)
    {
        printf("%i\n", array[i]);
    }
    return;
};

//DONDE SE LLAMARAN LAS FUNCIONES////
int main(){
    fillArray(myIntArray, 5); //aqui estamos llamando la funcion para llenar los valores del array, cuyo tamaño es 5
    printArray1D(myIntArray, 5); //aqui estamos llenando los printf y mostrandolos, por lo que debemos poner el mismo tamaño que el array
    return 0;
}



