#include <stdio.h>
// #include "./utils.h" sin carpeta, y el otro es desde carpeta
#include "/mnt/c/Users/manan/StructuredPrograming2A/unit2/folderTest/utils.h"

int myNumber = 3;
float myfloat = 3.1416;
char myString[255] = "Hola mundo"; //caracteres que tendra el mundo


// Primer metodo para funciones
//Declare and define the function or variable
// void sayHello( char message[]){
//         printf( "%s\n", message);
    
// }

    //segundo metodo para funciones
    // 1- declaro
void sayMyname ( char message[]);

int addTwoNumbers( int argumento1 , int argumento2 ); //declarando Conocido tambien como el prototipo de la función;

int main( ){

        sayHello("Hola mundo");
        sayMyname("Luis");
        int myResult = addTwoNumbers ( 2, 5);
        printf ("myResult is equal to: %d \n", myResult);
        return 0;  
}

// 2-definimos
// void sayMyname ( char message[]){
//         printf( "%s\n", message);
// }

// int addTwoNumbers( int argumento1, int argumento2){  
//         int result = argumento1 + argumento2;
//         return result;

// }