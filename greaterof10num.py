# ### 🐍 Next Problem: Count Numbers Greater Than 10

# Create a list of **8 numbers**.

# Write a program that:

# 1. Goes through each number using a `for` loop.
# 2. Checks if the number is greater than `10`.
# 3. Counts how many numbers are greater than `10`.
# 4. Prints the final count.

# **Example:**

# numbers = [4, 15, 7, 22, 31, 3, 9, 18]

# Output:
# Numbers greater than 10: 4

# **Topics:** List, `for` loop, `if`, comparison (`>`), counter variable.

nums = [2,16,15,25,30,26,28,40]
count = 0
for num in nums:
    if num >= 10:
        count += 1
print(count)

#====================#
# below correet answer

# nums = [2, 16, 15, 25, 30, 26, 28, 40]

# count = 0

# for num in nums:
#     if num >= 10:
#         count += 1

# print(count)