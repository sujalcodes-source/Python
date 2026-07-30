
#my code wrong answer 

# name = input("Enter your name")
# vowals = ["a","e","i","o","u"]
# for i in name:
#     if(name == vowals):
#         print(f"There are vowals in your name")
#     print("your name do not have vowals")
#correct code | below

text = input("Enter a string: ")
#take input of the name / text etc
count = 0
#now we keep the count to 0 at start
for char in text.lower():
    if char in "aeiou":
        #the if block say that if there aeiou  in the name then in the count which at start 0 by 1 unit
        count += 1
#print after the for loop ends
print("Number of vowels:", count)