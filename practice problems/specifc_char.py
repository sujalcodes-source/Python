# ### 🐍 Next Problem: Count a Specific Character

# Write a Python program that:

# 1. Creates a string:

#    ```python
#    text = "programming is fun"
#    ```
# 2. Asks the user to enter a character.
# 3. Uses a `for` loop to check every character in the string.
# 4. Counts how many times that character appears.
# 5. Prints the count.

# **Example:**

# ```text
# Enter a character: m

# 'm' appears 2 times.
# ```

# ### 📚 Topics used

# * String
# * `input()`
# * `for` loop
# * `if` statement
# * Counter variable
# * `==` operator

chars = input("Enter your char :")
count = 0 
text = "MY NAME IS SUJAL"

for char in text:
    if ( char == chars):
        count += 1
print(count)


