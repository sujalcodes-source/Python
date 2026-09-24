
# # 🟢 Problem 6

# **Topic:** `if/elif/else` + logical conditions
# **Difficulty:** ⭐⭐ Easy → Medium
# **Goal:** Combine multiple conditions into a real-world decision.

# Write a program that takes a person's **age** and determines their category:

# * `0–12` → Child
# * `13–17` → Teenager
# * `18–59` → Adult
# * `60+` → Senior Citizen

# Also handle an invalid age such as `-5`.

# **Example:**

# ```text
# Enter your age: 21
# You are an Adult

age = int(input("Enter your age :"))
if(age==0 or age >0):
    print("child")
elif(age == 13 or age < 17):
    print("Teenager")
elif(age == 18 or age <59):
    print("Adult")
else:
    print("Senior citizen")