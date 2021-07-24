import sys


def AverageValue(MyList):
    result = 0

    for MyList in range (1, len(sys.argv)):
        result = (result + float(sys.argv[MyList]))
    Average = result/MyList
    return Average

if __name__ == "__main__":
    print("Initializing program...")
    print("Average Value:", AverageValue(sys.argv)) 
    
   