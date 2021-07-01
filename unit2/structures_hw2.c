#include <stdio.h>
#include <string.h>
#include "./folderTest/utils.h"


int main(int argc, char** argv){
    
    int NewInt= 9;
    int NewInt_2= 8;
    int multiplo= 2;
    

    UTILS myStructC= {1, ShowIntAdress, ShowIntValueAdress, modifyVariablesAddress};
    printf("myInt: %d , &myStructC:%p\n", myStructC.myInt, &myStructC);
    UTILS* myStructP=&myStructC;
    printf("myInt: %d\n", (*myStructP).myInt);

    printf("------------------\n");
    myStructC.ShowIntAdress(&NewInt);
    printf("------------------\n");
    myStructC.ShowIntValueAdress(&NewInt);
    printf("------------------\n");
    myStructC.modifyVariablesAddress(&NewInt, &NewInt_2, multiplo);
    printf("Int_1=  %i, Int_2= %i\n", NewInt, NewInt_2);
    printf("------------------\n");
    
    return 0;
}