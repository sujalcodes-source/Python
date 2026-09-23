# ### 🐍 Next Problem: Count Vowels

# Write a Python program that:

# 1. Creates a string containing a sentence or word.
# 2. Uses a `for` loop to check each character.
# 3. Counts how many vowels (`a, e, i, o, u`) are present.
# 4. Prints the total number of vowels.

# **Example:**

# ```python
# text = "programming"
# ```

# Output:

# ```text
# Number of vowels: 3
# ```

# ### 📚 Topics used

# * String
# * `for` loop
# * `if` statement
# * `in` operator
# * Counter variable
sen = "Hi my name is Sujal and i am a student studying cs :)"
vowels = "aeiou"
count = 0 
for sens in sen:
    if sens in vowels:
        count += 1
print(count)   