from sys import argv as ag


def addToNumbers( number1, number2):
    print('StartProgram: addToNumbers executed...\n')
    result = number1+number2

    return result


if __name__ == "__main__":
    print(f' La suma de los dos numeros = { addToNumbers( int(ag[1]), int(ag[2])) }' )