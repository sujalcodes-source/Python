# 🟢 Problem 5: Count Positive Numbers
# Create a list containing positive and negative numbers. Count how many numbers are positive.
# # Topics: List, for loop, if, counter
# this is what a counter is 
# from collections import Counter

# # # Create a list of items
# # a = [1, 1, 1, 2, 3, 3, 4]

# Use Counter to count occurrences
# cnt = Counter(a)
# print(cnt)

# code here below :
numbers = [23,-44,3, 34, -433,-22, 36,26]
for num in numbers:
    if(num > 0):
        print(f"The number is positive {num}")
    else:
        print(f"The number is negative {num}")

        
