#include <stdio.h>
#include <stdlib.h>

///USANDO PONTERS Y DIRECCIONES PARA GUARDAR VALORES Y MODIFICARLAS MEDIANTE OPERACIONES///
//NOTA: esto es necesario ya que no podemos almacenar en una variable que no sea pointer la operación que sea ejecutada y arrojar luego los nuevos valores 
int var1 = 10;
int var2 = 20;

void  modifyVariables( int* argumento1, int* argumento2){
    *argumento1 = *argumento1*2;
    *argumento2 = *argumento2*2;
    return;
}

void SwapVar(int*SwVar1, int*SwVar2){
    int temporal = *SwVar1;
    *SwVar1 = *SwVar2;
    *SwVar2 = temporal;
}


int main ( int argc, char** argv){
        printf( "var1 =  %d, var2 =%d\n",  var1, var2 );
        printf("Funtion was executed:\n");
        int*NewVar1 = &var1;
        int*NewVar2 = &var2;
        printf("Adress_Var1:%p, Adress_Var2:%p\n", &var1, &var2);
        modifyVariables(  &var1, &var2 );
        printf("var1=  %d, var2= %d\n", var1, var2 );
        
        printf("------------------------------------\n");
        printf("Executing swap program....\n");
        SwapVar(&var1, &var2);
        printf("var1=  %d, var2= %d\n", var1, var2 );
        return 0;
}