
# Write a Python program that takes a sentence from the user and counts how many vowels (`a, e, i, o, u`) it contains.

# **Example:**

# ```text
# Enter a sentence: Python is amazing
# Number of vowels: 5
# ```
sentence = input("Enter your sentence")
for vowels in sentence:
    vowel= "aeiou"
    if(sentence == vowel):
        print("There is vowels present")
    else:
        print("There are no vowels")
# correct answer

# sentence = input("Enter a sentence: ")

# vowels = "aeiou"
# count = 0

# for char in sentence.lower():
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)