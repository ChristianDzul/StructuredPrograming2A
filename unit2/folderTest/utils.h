#include <stdio.h>
#include <stdlib.h> //atoi, atof, sprinf,
#include <string.h> //strcpy

//se pueden guardar macros o variables (las cuales son globales )
#define pi 3.1416
//int libInteger = 24;

//objeto//
typedef struct utils
{
        int myInt;
        void (*ShowIntAdress) (int* param);
        void (*ShowIntValueAdress) (int* param);
        void (*modifyVariablesAddress) (int* dir1, int* dir2, int multiplo );
}UTILS;
// typedef struct utils
// {
//         int myInt;
//         void (*ShowIntAdress) (int* param);
//         void (*mySwap) (int* ptr1, int* ptr2);
        
// }UTILS;

typedef struct  array
{
        int dirArray[2];
        float aFloat;
        float * aFloatPointer;
}Array;


int libInteger = 24;

//---FUNCTIONINTRO.C//
void sayHello( char message[]){
        printf( "%s\n", message);
    
}

void sayMyname ( char message[]){
        printf( "%s\n", message);
        return;
}

int addTwoNumbers( int argumento1, int argumento2){  
        int result = argumento1 + argumento2;
        return result;
}

void modifyVariables( int argumento1, int argumento2){
        argumento1 = argumento1*2;
        argumento2 = argumento2*2;
        return;
}
///----AQUI TERMINA----///

// paso de argumentos por valor//
 

// paso de argumentos de dirección//
// void modifyVariablesAdress(int*ptr1, int*ptr2){
//         *ptr1 = *ptr1*2;
//         *ptr2 = *ptr2*2;
//         return;

// }
void ShowIntAdress(int* param){         
        printf("adress: %p\n", param);
}

void ShowIntValueAdress(  int* param  ){
        printf( "value: %i\n", *param );
}

void ShowFloatAdress(  int* param  ){
        printf( "address: %p\n", param );
}

void modifyVariablesAddress( int* dir1   ,  int* dir2, int multiplo ){
        ShowIntAdress(dir1);
        ShowIntValueAdress(dir1);
        ShowIntAdress(dir2);
        ShowIntValueAdress(dir2);
        *dir1 =  *dir1 * multiplo;
        *dir2 =  *dir2 * multiplo;
        return;
}

void swap( int* ptr1, int* ptr2){
        int temp = *ptr1; 
        *ptr1 = *ptr2;
        *ptr2 = temp;
        return;
        printf("Hola munda!");
}

// void swapGobal(){
//         int temp = myVar1;
//         myVar1 = myVar2;
//         myVar2 = temp;
//         return;
// }

//----------------------------My actividad del swap------------------------//
void ShowIntNewValue(int* param){
        printf("Value: %i\n", *param);

}

int SwapVariables(int*dir1, int*dir2){
        printf("This the adress and value of Num1:\n");
        ShowIntAdress(dir1);
        ShowIntNewValue(dir1);
        printf("This the adress and value of Num2:\n");
        ShowIntAdress(dir2);
        ShowIntNewValue(dir2); 
        int tmp;
        tmp = *dir1;
        *dir1 = *dir2;
        *dir2 =  tmp;
        return 0;
}
//--------------------------------------------------------------------------//

void fillArray(int array[], size_t tam){
        for (size_t i = 0; i < tam; i++)
        {
                array[i] = i*2;
        }
        return;
}

void PrintArray1D(int array[], size_t tam){
for (size_t i = 0; i < tam; i++)
        {
               printf("%i\n", array[i]); 
        }
        return;
}

Array* returnArray( ){
        // int unArreglo[5] = {1,5,6,7,8};
        Array* unArrayType = (Array*)malloc(sizeof(Array) ); //esta funcion de malloc te permirte crear otra estructura que englobe a la estructura de tipo array, por ello se usa el "*" para llamar la direccion y pasarla a una nuesva estruc que sera ampliada por la funcion malloc
        printf("addres unArrayType: %p, unArrayType = %p \n",  &unArrayType, unArrayType );

        unArrayType->dirArray[0] = 17;
        unArrayType->dirArray[1] = 15;
        return unArrayType;
}

//--------------------------------------------------------------------//


