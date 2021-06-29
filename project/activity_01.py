import sys

num1 = 9

def isPrime( ):
    #def message():
      #  print("It is function")
    global num1
    num1 = 3
    def localfunction():
        print("This is a local function")

    localfunction()
    message()

    num_div = 1
    count = 2 #dos cuentas

    if(num1 == 1):
        print("It is not prime")
        exit()
    while (count <= num1):
        if( num1 % count == 0):
            num_div += 1
        count +=1
    if(num_div > 2):
        return False
    else:
        return True

def message( ): #Global
    print("Global var")


def powTwoNumbers(num1, num2):
    powNum1 = pow(num1, 2)
    powNum2 = pow(num2, 2)
    return (powNum1, powNum2)

#(a , b) = ("hola", "luis")


if __name__ == "__main__":
    #print ( a, b)

    print(f'num1:{num1}')

    print( isPrime()   )

    print(f'num1:{num1}')
    
    (x, y) = powTwoNumbers (2, 3)

    print (f'x:{x} , y:{y}')

   # print( powTwoNumbers() )