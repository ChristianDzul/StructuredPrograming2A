#include <stdio.h>
#include <stdlib.h> //atoi, atof
#include <stdbool.h> //TRUE OR FALSE



#define TAN 10 ///una macro definida con su tamaño de 10 en este caso, no lleva ; ni signo de = en una macro

int lista[TAN] = {105,20,21,40,33,60,70,50,93,100}; //creamos un array, que tambien puede ser int list[10] =  {}
int idx = 0;

//typedef int INTEGER; , esto permite darle un mote a un tipo de variable.En este caso todas las varibales con "int" ahora pueden llamarse INTEGER

int main(int argc, char** argv){    ///opcional si no las vamos a usar

    int index2 = 0;
    for(int index = 1; index <= TAN; index++, index2++){  //puedo tener dos potenciadores-incrementadores pero no puedo tener dos inicializadores.El incrementador puede ser dos formas, index = index +1 , o index++                        //index <= TAN, en el lugar de "TAN" puede ser un variable como lo es este, o un numero especifico, lo cual indica la condicion a cumplir
        printf("index: %d, value: %d. \n\a", index, lista[index]);
        // for (INTEGER i = 0; i < count; i++) sirve para hacer loops infintos, un bucle anidado
        // {     //i < count es la condicion que se seguira ejecutando hasta que ya no se cumpla
        //     /* code */
        // }
        
    }

    while (true)    ///mientras sea true estaras buscando el dato
    {  
        if( lista[idx]== 50 ){ ///si este dato lista contiene el dato 50 que estoy buscando
            break;  //en ese caso rompres el programa, esta palabra-funcion reservada sirve para romper un bucle mas cercano
        }
        idx++;
    }
    printf("idx found: %d\n", idx); //marca el valor de 50 dentro del index, es decir, su posición


    //Segunda forma de como hacerlo

    int idx_for = 0; //definimos idx_for para el "for"
    for ( ; lista[idx_for] != 50; idx_for++){ } //se puede omitir el inicializador y dejar el espacio vacio
    printf("idx_for found:%d\n", idx_for);
    return 0;
}