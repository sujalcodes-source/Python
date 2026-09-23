# 🟢 Problem 5

# Topic: Nested if + logical thinking
# Difficulty: ⭐⭐ Easy

# Write a program that asks for:

# username
# password

# The correct username is:

# admin

# The correct password is:
# 1234

# If both are correct → "Login successful"

# If username is wrong → "Invalid username"

# If username is correct but password is wrong → "Invalid password"

# Try it yourself first.
uname = input("Enter your user name : ")
passWord = int (input("Enter your password"))
if(uname == "Admin"):
    if(passWord == 1234):
        print("---LOGIN SUCCESSFULL")

if(uname !="Admin"):
    print("You enter  the wrong user name")
    if(passWord !=1234):
        print("The password is wrong ")

#This is the correct code below : )

# uname = input("Enter your username: ")
# password = int(input("Enter your password: "))

# if uname == "admin":

#     if password == 1234:
#         print("LOGIN SUCCESSFUL")
#     else:
#         print("The password is wrong")

# else:
#     print("You entered the wrong username")

