import sys

Words=None
Reverse=None

def ReverseFrase(Reverse):
    Invertir =' '.join(reversed(Words.split()))
    print("\nReversed phrase: ", Invertir)
    return Reverse


if __name__ == "__main__":
    print("Reverse a string")
    print("Enter a phrase: ")
    Words= input()
    ReverseFrase(Reverse)
