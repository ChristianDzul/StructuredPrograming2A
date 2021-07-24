import sys 


def AddTwoNumbers (num1, num2):
    addition = num1 + num2
    return addition

def SubtractTwoNumbers (num1, num2):
    subtraction = num1 - num2
    return subtraction

def MultiplicationTwoNumbers (num1, num2):
    multiplication = num1*num2
    return multiplication

def DivisionOfTwoNumbers (num1, num2):
    division = num1/num2
    return division

if __name__ == "__main__":
    print("Initializing program calculator...\n")
    print(f'Additon result:{AddTwoNumbers(float(sys.argv[1]),float(sys.argv[2]))}')
    print(f'Subtraction result:{SubtractTwoNumbers(float(sys.argv[1]),float(sys.argv[2]))}')
    print(f'Multiplication result:{MultiplicationTwoNumbers(float(sys.argv[1]),float(sys.argv[2]))}')
    print(f'Division result:{DivisionOfTwoNumbers(float(sys.argv[1]),float(sys.argv[2]))}')