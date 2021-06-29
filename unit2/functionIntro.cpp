#include <istream>

std::string myString = "Hola mundo";
int myNumber = 3;
float myFloat = 3.1416;

// Declarando
void sayHello(std::string tag1 );


int main(){

        sayHello(myString);

        return EXIT_SUCCESS;
}

// Define
void sayHello( std::string tag1 ){
    std::cout<<tag1<<std::end1;

}