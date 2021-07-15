#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./folderTest/utils.h"

//arrays
int myIntArray[5];

int myInt = 4;
float myFloat = 3.1416;


typedef struct mago{ //el typedef sirve para poder hacer que el nombre de la estructura tenga un alias que nosotros queramos

        int vida;
        int mana;
        char* nombre;
        //mas atributos//
        //sayHello
        void (*Saludo) (char message[]);
        int (*sumaDosNumeros) (int  argumento1, int argumento2 );
}Mago; //esto es un tag que tu asignas a la estructura

// typedef struct mago Mago;

int main(){
        
        Mago luis = { 100, 100, "Luis_Gerardo", sayHello, addTwoNumbers };
        struct mago miguel = {200, 200, "Miguel"};
        
        
        printf( "%s\n", luis.nombre  ); //en pointer, el "." se usa cuando quieres acceder a algo dentro de una estructura array
        luis.Saludo( "Hola soy un mago!");
        printf( "%d\n"  , luis.sumaDosNumeros(20,25)   );
        
        fillArray( myIntArray, 5);
        PrintArray1D( myIntArray,  5   );
        printf("%d",  myIntArray[0]   );
        printf("%d",  myIntArray[1]   );
        printf("%d",  myIntArray[2]   );
        printf("%d",  myIntArray[3]   );
        printf("%d",  myIntArray[4]   );
        
        Array* myArray =  returnArray();
        printf(  "\n%d ", myArray->dirArray[0] );
        printf(  "\n%d ", myArray->dirArray[1] );
        printf(  "\n%d ", myArray->dirArray[2] );

        return 0;
}
