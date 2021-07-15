#include <stdio.h>
#include "/mnt/c/Users/manan/StructuredPrograming2A/unit2/folderTest/exercise_07.h"

int main(){

ROBOT markovito;
markovito.name = "Markovito";
markovito.type = "ServiceRobot";
markovito.height = 1.2;
markovito.weight = 2.5;
markovito.degreesOfFreedom = 3;

markovito.sayHelloToRobot = sayHelloToRobot;
//sayHelloToRobot(markovito);

ROBOT tiago;
tiago.name = "Tiago";
tiago.type = "ServiceRobot";
tiago.height = 1.7;
tiago.weight = 2.8;
tiago.degreesOfFreedom = 7;
tiago.sayHelloToRobot = sayHelloToRobot;
//sayHelloToRobot(tiago);
markovito.sayHelloToRobot(tiago);
 return 0;
}





