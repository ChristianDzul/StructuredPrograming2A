#include <stdio.h>
// #include "./utils.h" sin carpeta, y el otro es desde carpeta
#include "/mnt/c/Users/manan/StructuredPrograming2A/unit2/folderTest/utils.h"

int myNumber = 3;
float myfloat = 3.1416;
char myString[255] = "Hola mundo"; //caracteres que tendra el texto, cadena de caracteres como maximo

//PRIMER METODO: DECLARAR Y DEFINIR UNA FUNCION (dos en uno)-----------------------
// void sayHello ( char message[]  ){ //poner el type del argumento, en este caso es un char string el parametro-etiqueta "message"
//     printf("%s", message);  
// }    //esta funcion lleva void ya que no retorna o arroja un dato u operación, solo lo hace pero no arroja nada (tal como un numero)
//_--------------------------------------------------------------

//----SEGUNDO METODO PARA FUNCIONES: 1-Declaro
void sayMyname ( char message[]);

int addTwoNumbers( int argumento1 , int argumento2 ); //declarando Conocido tambien como el prototipo de la función;
//------------------------------------//

int main( ){  ///dentro de esto va el llamado de las funciones. Las funciones pueden ir abajo o arriba. RECORDAR QUE CUANDO MAIN SE EJECUTA HACE EL BARRIDO (ARRIBA-ABAJO) PARA BUSCAR LAS FUNCIONES LLAMADAS DENTRO DE MAIN    

        sayHello("Hello World");
        sayMyname("Luis");
        int myResult = addTwoNumbers ( 2, 5);
        printf ("myResult is equal to: %d \n", myResult); 
        return 0;  
} 

// -------2-definimos-----------------------------------//
// void sayMyname ( char message[]){
//         printf( "%s\n", message);
// }

// int addTwoNumbers( int argumento1, int argumento2){  
//         int result = argumento1 + argumento2;
//         return result;

// }

//----------------------------------------------------//