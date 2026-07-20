# Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 

#My answer
year=2026
name=input("Enter your name ")
age=input("Enter your age ")
age=int(age)
#the logic here is currentyear+yourage+100  2026−19+100
print(year-age+100)


#refer solution
# name = input("Enter your name: ")
# age = int(input("How old are you turning in the current year?: "))
# currentYear = int(input("Enter current year: "))
# yearOfBirth = currentYear - age
# print(f'{name}, you will turn 100 years old in {yearOfBirth+100}')