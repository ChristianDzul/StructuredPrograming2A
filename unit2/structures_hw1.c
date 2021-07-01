#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./folderTest/utils.h"

//Arrays//
int myNewIntArray[6];

typedef struct precios_carros{
    float Ferrary;
    float Mercedes;
    float Volkswagen;
    float Nissan;
    float Toyota;
    char* client_name;
}Precios;
 
float main(){
    Precios Client_1 = {11500000.12, 9456000, 6000450.2, 5798000, 4998045.70,"Christian" };
    Precios Client_2 = {11500000.12, 9456000, 6000450.2, 5798000, 4998045.70,"Luis" };
    printf("List of prices for client 1:\n");
    printf("Ferrary: %f\nMercedes: %f\nVolkswagen: %f\n", Client_1.Ferrary, Client_1.Mercedes, Client_1.Volkswagen);
    printf("Nissan: %f\nToyota: %f\nClient Name: %s\n", Client_1.Nissan, Client_1.Toyota, Client_1.client_name);
    // client 2//
    printf("//////////////////////////////////////////////////\n");
    printf("List of prices for client 2:\n");
    printf("Ferrary: %f\nMercedes: %f\nVolkswagen: %f\n", Client_2.Ferrary, Client_2.Mercedes, Client_2.Volkswagen);
    printf("Nissan: %f\nToyota: %f\nClient Name: %s\n", Client_2.Nissan, Client_2.Toyota, Client_2.client_name);
    return 0;
}