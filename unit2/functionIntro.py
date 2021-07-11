from sys import argv as ag


def addToNumbers( number1, number2): ##dentro no pueden ir numero ya que solo son permitidas  etiquedas o alias
    print('StartProgram: addToNumbers executed...\n')
    result = number1+number2

    return result  ##or its also possible to put "retur number1 + number2"
    

answer = False  ##creacion de una variable booliana, almacena info y puedo acceder a ella en cualquier parte del codigo

##FUNCION PARA VER SI UN NUMERO ES PAR O IMPAR##
def isEven(aNumber): 
    if(aNumber%2 == 0):
        return True
            #print("It's even")
    else:
        return False
            #print("It's odd!")

if __name__ == "__main__":
    # print(f' La suma de los dos numeros = { addToNumbers( int(ag[1]), int(ag[2])) }' ) // argv [numero a que haces alucion de la lista]
   ##el argv o ag en este caso es para que podamos ingresar un valor manual y no setear uno especifico, lo cual es posible si quieres
   

   ##Other way to do it
    n1 = int(input('Dame numero 1:\t' ))      
    n2 = int(input('Dame numero 2:\t'))
     ##print(f' La suma de los dos numeros = { addToNumbers( n1, n2 )}' ) // si lo dejo estariamos haciendo dos llamadas

    ##answer = isEven( addToNumbers( n1, n2) ) ##---funcion dentro de una funcion, o mejor conocido como stack, donde resuelve primero el argumento

    # isPrime(n1)
    # isPrime(n2)

    

    if(isEven( addToNumbers( n1, n2) )):
        print(f'N1: "{n1}" and N2: "{n2}" are your lucky numbers!')
    else: 
        print(f'N1: "{n1}" and N2: "{n2}" are not your lucky numbers!')

    # if (isPrime(n1)):
    #     print("n3 is prime")
    # else:
    #     print("n3 is not prime")
    # if( isPrime (n4))