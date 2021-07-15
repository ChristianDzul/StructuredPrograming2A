#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./folderTest/utils.h"

// typedef struct utils {
//         int myInt;
// }UTILS;

int a = 2;
int b = 4;

int main(int argc, char** argv){

        int otroInt = 9;
        UTILS myStructC = {1,ShowIntAdress}; //adding the function to link
        printf("myInt: %d. &myStructC: %p\n", myStructC.myInt, &myStructC );
        UTILS* myStructP = &myStructC;
        printf("myInt: %d\n", (*myStructP).myInt );
        printf("myInt: %d\n", myStructP->myInt );
        myStructC.ShowIntAdress(&otroInt); //redirecciona la direccion de "otroInt" usando el ampersand

        UTILS obj; //no inicializada, no pasa nada
        //obj.myInt = 100; ejemploficacion de como crear una variable de utils y llmar la funcion de esta
        obj.mySwap = swap;
        obj.mySwap( &a, &b);
        printf("a:%d, b:%d.\n", a,b);
        return 0;
}