#include <iostream>

std::string myString = "Hola mundo"; // string esta contenida en la biblioteca std
int myNumber = 3; //no hereda de std
float myFloat = 3.1416;

// Declarando funcion
void sayHello(std::string tag1 );

//donde se llamara la funcion y arroja el resultado del proceso
int main(){

        sayHello(myString);

        return EXIT_SUCCESS;
}

// Definiendo funcion (el proceso que hara)
void sayHello( std::string tag1 ){
    std::cout<<tag1<<std::endl; ///<<std::end1 es el salto de linea

}