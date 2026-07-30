x = int(input("Enter your number"))
def evenodd():
    if(x % 2 == 0 ):
        print(f" {x} it is even")
        return "Even"
    else:
        print(f" {x} it is odd")
        return "Odd"
evenodd()