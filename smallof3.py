# ### 🟢 Problem

# Take **3 numbers** as input and print the **smallest number**.

# Example:

# ```text
# Enter: 10
# Enter: 5
# Enter: 8

# Smallest: 5
# Use `if`, `elif`, `else` and `and`.

# Try it yourself first. 💪

print("=== PLEASE ENTER YOUR NUMBER ===")
no1 = int(input("Enter your 1 num :"))
no2 = int(input("Enter your 2 num :"))
no3 = int(input("Enter your 3 num :"))

if ( no1 <no2 and no1 < no3):
    print(no1)
elif(no2 < no1 and no2 < no3 ):
    print(no2)
else:
    print(no3)
print("=== THANKS YOU :) ===")