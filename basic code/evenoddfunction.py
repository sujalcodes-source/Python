x = int(input("Enter your number :"))
def evenodd():
    if(x % 2 == 0):
        print(f"This number {x} is even")
        return "even"
    else:
        print(f"This number {x} is odd")
evenodd()
