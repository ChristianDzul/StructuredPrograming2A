##Start##
print ("Welcome to the greatest number calculator")

##Variables##
num1 = 0
num2 = 0
num3 = 0

##Getting the values##
num1 = int( input("Insert a value for number 1 \n"))
num2 = int( input("Insert a value for the number 2 \n"))
num3 = int( input("Insert a value for the number 3 \n"))

print ("Finding the greatest number...")
print ("Please wait...")
##Process##

if ( num1 == num2 == num3):
    print ("All numbers are the same", num1, num2, num3)
elif (num1 > num2):
    if (num1 > num3):
        print ("The number 1 is the greatest number:", num1, num2, num3)
elif (num2 > num3):
    print ("The number 2 is the greatest number", num1, num2, num3)
else:
    print ("The number 3 is the greatest number:", num1, num2, num3)
