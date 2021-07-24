import sys

def CallingMont():
    for month in range (1,13):
        print(f"Month:{month}")
        if month == 2 :
            for day in range (1,29):
                print (f"  Day:{day}")
        elif month == 4:
            for day in range (1,31):
                print (f"  Day:{day}")
        elif month == 11:
            for day in range (1,31):
                print (f"  Day:{day}")
        elif month == 9:
            for day in range (1,31):
                print (f"  Day:{day}")
        elif month == 6:
            for day in range (1,31):
                print (f"  Day:{day}")        
        else: 
            for day in range (1,32):
                print (f"  Day:{day}")
    return 0

if __name__ == "__main__":
    print("Starting Program\n")
    print("Please wait...\n")
    CallingMont()
    