# ### 🐍 Next Problem: Sum of Even Numbers

# Create a list:

# ```python
# numbers = [5, 12, 7, 20, 8, 15, 30]
# ```

# Write a program that:

# 1. Goes through the list using a `for` loop.
# 2. Checks which numbers are **even**.
# 3. Adds all the even numbers together.
# 4. Prints the final sum.

# Expected output:

# ```text
# The sum of even numbers is 70
# ```

# ### 📚 Topics used

# * List
# * `for` loop
# * `if` statement
# * `%` operator
# * Variable
# * Addition

nums = [1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if(num % 2 == 0):
        even_sum = num+num
print(even_sum)

#======================================#
#THIS IS MORE CORRECT QUESTION BELOW

# nums = [1,2,3,4,5,6,7,8,9,10]

# even_sum = 0

# for num in nums:
#     if num % 2 == 0:
#         even_sum = even_sum + num

# print(even_sum)