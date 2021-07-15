#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include "./folderTest/utils.h"
#include "stdbool.h"

void callToNumber(int number){
        //Logica compleja para llamar a un numero//
        printf("Llamando al %d...!\n", number   );
}
//Declarando
void SecurityCamera( void (*cb) (int number),  int  EmergencyNumber );
void SecurityCamera2(); //funcion esperando a que algo pase

int main(){
        
        // for(;;){
                SecurityCamera( callToNumber, 911  );

        // }
        return 0;
}
//Defi
void SecurityCamera( void (*cb) (int number), int EmergencyNumber   ){
        //Logica Compleja//
        bool thief = false;
        //puts ("CACA"); //similar a la funcion PRINTF
        if(thief){ //Si detecta ladron debe hacer algo!
                // Ejecutar un calback
                callToNumber(EmergencyNumber);
        }
}

void SecurityCamera2(){

        callToNumber(999);
}