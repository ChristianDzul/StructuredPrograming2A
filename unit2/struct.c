#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./folderTest/utils.h"

typedef struct utils {
        int myInt;
}UTILS;



int main(int argc, char** argv){

        UTILS myStructC = {1};
        printf("myInt: %d. &myStructC: %p\n", myStructC.myInt, &myStructC );
        UTILS* myStructP = &myStructC;

        printf("myInt: %d\n", (*myStructP).myInt );
        printf("myInt: %d\n", myStructP->myInt );



        return 0;
}