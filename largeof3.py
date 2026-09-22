# ### 🟡 Next Problem
# Take **3 numbers** as input and print the **largest number**.
# **Example:**
# ```text
# Enter numbers: 10 25 7
# Largest: 25
# ```
# Use only `if`, `elif`, `else`.
print("=== PLEASE ENTER YOUR NUMBER ===")
no1 = int(input("Enter your 1 num :"))
no2 = int(input("Enter your 2 num :"))
no3 = int(input("Enter your 3 num :"))

if ( no1 >no2 and no1 > no3):
    print(no1)
elif(no2 > no1 and no2 > no3 ):
    print(no2)
else:
    print(no3)
print("=== THANKS YOU :) ===")