
#  🟢 Problem 2
# Topic:** `if / elif / else` + modulo `%` operator
# Difficulty:** ⭐ Easy
# Goal:** Learn to use the remainder operator to build logic.

# ### Question

# Take an integer from the user and determine whether it is:

# * **Even**
# * **Odd**

#NOTE = In Python, the number zero is considered even.  This is because zero is divisible by 2 with a remainder of 0, satisfying the mathematical definition of an even number. 



number = int(input("Enter your number"))
if(number % 2 == 0):
    print("The number is even")
elif(number % 2 !=0):
    print("The number is odd")
else:
    print(f"The number is you is invaild or zero here is your number {number}")

# #this can also be a answer 
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")