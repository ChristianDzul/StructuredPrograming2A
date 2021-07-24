import sys

tempF = [63,73,-999,91,86,82,72,81,66,77,75,104,-999,84,77,66,82,63,93,72,82,64,75,90,64,-999,99,82,95,82]
tempC = []
x = 5/9   

def ConversionToCelsius (Conversion):
    for Conversion in range (0, len(tempF)):
       tempC.append(round((tempF[Conversion]-32)*(x), 2))
    print("List in Celsius",tempC) 

def AverageOfTempC (Average):
    for Average in range (0, len(tempC)):
        Average = sum(tempC)/len(tempC)
    return Average

if __name__ == "__main__":
    print("STARTING PROGRAM!!!")
    print("-------------------------------")
    print("Original List:\n", tempF)
    tempF.pop(2 )
    tempF.pop(11)
    tempF.pop(23)
    print("-------------------------------")
    print("Removing Non-Relevant Data!!!")
    print("NewList:\n", tempF)
    print("-------------------------------")
    ConversionToCelsius (tempC)
    print("-------------------------------")
    print("Maximun Value of TempC:", max(tempC))
    print("Average Value of TempC:", AverageOfTempC(tempC))
    