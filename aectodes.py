#🔥 Next Python Problem

# Take **3 numbers** and print them in **ascending order** (smallest → largest).

# Example:

# ```text
# Input: 8, 3, 5
# Output: 3 5 8
# ```

# **Hint:** Try using only `if/elif/else` and comparisons.


number1 = int(input("ENTER YOUR  NUMBER :"))
number2 = int(input("ENTER YOUR  NUMBER :"))
number3 = int(input("ENTER YOUR  NUMBER :"))

if(number1 < number2 and number1 < number3):
    print(number1)
elif(number2 < number1 and number2 < number3):
    print(number2)
else:
    print(number3)