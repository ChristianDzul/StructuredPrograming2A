import sys

def isPrime(num1):
    message("This is a function...")    
    #print("Initializing Prime Program...")
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

def message(string):
    print(string)

if __name__ == "__main__":
    print( isPrime( int(sys.argv[1] ) ) ) 







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
