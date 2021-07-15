#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct robot
{
    char* name;
    char* type;
    float height;
    float weight;
    int degreesOfFreedom;
    void (*sayHelloToRobot) (struct robot);

}ROBOT;


void sayHelloToRobot (ROBOT robot ){
        printf( "Hola %s\n", robot.name);
        return;
}
