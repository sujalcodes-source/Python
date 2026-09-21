# 🟢 Problem 4

# Topic: if / elif / else + logical operators (and, or)
# Difficulty: ⭐⭐ Easy
# Goal: Learn how to combine multiple conditions.

# Question

# Write a program that asks the user for:

# Age
# Whether they have a student ID (yes or no)

# A person can enter a student discount if:

# They are 18 or older AND have a student ID, OR
# They are under 18

a = int (input ("Enter your Age :"))
ID = input(" Do you have Student ID : ")
if( a >= 18   and ID == "Yes"):
    print("You get the student discount")
elif( a <= 18):
    print("You are not 18")
else:
    print("Sorry you cant get the student discount")


#This is the correct code below

# age = int(input("Enter your age: "))
# ID = input("Do you have a Student ID? ")

# if age >= 18 and ID == "yes":
#     print("You get the student discount")

# elif age < 18:
#     print("You get the student discount")

# else:
#     print("Sorry, you can't get the student discount")