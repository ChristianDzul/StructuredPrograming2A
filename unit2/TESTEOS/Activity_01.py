import sys

num1 = 9 ##variable global

def isPrime():
    # message("This is a function...")    
    #print("Initializing Prime Program...")
    global num1 ##esta funcion global dentro de una función permite que la variable apesar de ser previamente definida, este pueda ser modificada y se vea reflejada dentro de la variable
    num1 = 3
   
    def localFuction():
        print("This is a local function")
    # localFuction() ##var local
    # message() ##var local
   
   
   
   
    num_div = 1
    count = 2 ##dos cuentas

    if(num1 <=1):
        print("its not prime")
        exit()
    while(count <= num1):
        if(num1 % count == 0):
            num_div += 1
        count += 1
    if(num_div>2):
        return False
    else:
        return True

def message(): ##global
    print("Global var")


def powTwoNumber(num1, num2): ##funcion en donde ingresaremos dos numeros cualquiera. el "num1" y "num2" no son mas que una etiqueta y no usara ninguna varibale (ni sus valores) que haya tenido ese mismo nombre
    powNum1 = pow(num1, 2)  ##La función "pow" elevara un numero base a una potencia (exponencial ) y retornara el resultado de hacer dicha operación
    powNum2 = pow(num2, 2) ##se lee de la siguiente forma "el valor que tenga num2 sera elevado a la potencia de 2"
    # print(powNum1, powNum2 ##para que elprint se ejecute hay que mandar a llamar a la funcion
    return (powNum1,powNum2)

(a,b) = ("hola", "luis") ##a esto se le conoce como una tupla, la cual sirve que si quieres usar "return" para retornar el resultado de mas de una variable, esto sea posible, ya que normalmente solo se puede 1


if __name__ == "__main__":
    # print( isPrime( int(sys.argv[1] ) ) )
    print(a,b)

    print(f'num1:{num1}') 

    print(isPrime())

    print(f'num1:{num1}') 
    (x,y) = powTwoNumber (2,3) ##asignado los valores a una variable para poder imprimir los valores de la tupla individualmete
    print(f'x:{x}, y:{y}') #usando la tupla para asignar el valor e imprimir individualmente el resultado
    # print(powTwoNumber (2,3)) ##usando return
    # powTwoNumber (2,3) ## setando numero fijos para el proceso pow--sin usar return
    #powTwoNumber (int(sys.argv[1]), int(sys.argv [2])) ##ingresando numeros cualquiera para para el proceso pow






##------------MY WAY TO IDENTIFY IF A NUMBER IS PRIME OR NOT-------------##
# def isPrime(num1):
#     if(num1 <=1):
#         print("It is not prime")
#     elif(num1 == 2):
#         print ("Its prime")
#     else:
#         for i in range (2, num1):
#             if(num1 % i == 0):
#                 return False
#         return True
# if __name__ == "__main__":
#     print(isPrime(int(sys.argv[1])))
