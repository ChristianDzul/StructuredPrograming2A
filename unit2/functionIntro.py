from sys import argv as ag


def addToNumbers( number1, number2):
    print('StartProgram: addToNumbers executed...\n')
    result = number1+number2

    return result

answer = False

def isEven(aNumber):
    if(aNumber%2 == 0):
        return True
            #print("It's even")
    else:
        return False
            #print("It's odd!")

if __name__ == "__main__":
    # print(f' La suma de los dos numeros = { addToNumbers( int(ag[1]), int(ag[2])) }' ) // argv [numero a que haces alucion de la lista]
    n1 = int(input('Dame numero 1:\t' ))
    n2 = int(input('Dame numero 2:\t'))


    isPrime(n1)
    isPrime(n2)

    ##print(f' La suma de los dos numeros = { addToNumbers( n1, n2 )}' ) // si lo dejo estariamos haciendo dos llamadas

    #answer = isEven( addToNumbers( n1, n2) )

    if(isEven( addToNumbers( n1, n2) )):
        print(f'N1: "{n1}" and N2: "{n2}" are your lucky numbers!')
    else: 
        print(f'N1: "{n1}" and N2: "{n2}" are not your lucky numbers!')

    # if (isPrime(n1)):
    #     print("n3 is prime")
    # else:
    #     print("n3 is not prime")
    # if( isPrime (n4))