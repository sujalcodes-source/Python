# Problem 5
# Given a list of numbers, count how many numbers are greater than 10.
# # Topic: List, for loop, if, counter

def num():
    numbers = [10,23,54,74,25,7,52,7,8,1]
    for number in numbers:
        if(number > 10):
            print(f"The number is greater than 10 :- {number}")

num()