# 🟢 Problem 1

# Topic: if / elif / else + comparison operators
# Difficulty: ⭐ Easy
# Goal: Practice decision-making logic.

# Question:
# Take a number from the user and print whether it is positive, negative, or zero.

#the normal input takes a string we need to specific the datatype
num = int(input("Enter your number : "))
if(num > 0):
    print(f"The number your enter is {num}  and the number is positive")
elif(num < 0 ):
    print(f"The number your enter is {num} and the number is negative")
else:
    print(f"The number your enter is {num} and the number is zero ")