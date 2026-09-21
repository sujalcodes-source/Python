
# # 🟢 Problem 3
# **Topic:** `if / elif / else` + multiple conditions
# **Difficulty:** ⭐⭐ Easy
# **Goal:** Practice combining conditions and building a decision system.

# ### Question

# Write a program that takes a student's **marks (0–100)** and prints their grade:

# |    Marks | Grade |
# | -------: | :---- |
# |   90–100 | A     |
# |    80–89 | B     |
# |    70–79 | C     |
# |    60–69 | D     |
# | Below 60 | F     |

M = int(input("Please Enter your marks :"))
if(100 < M < 90):
    print(f"This is your marks {M} and your grade is A+ ")
elif(80 > M  <89 ):
    print(f"This is your marks {M} and your grade is B")
elif(70 > M < 79 ):
    print(f"This is your marks {M} and your grade is C")
elif(60 > M < 69):
    print(f"This is your marks {M} and your grade is D")
elif(M < 60):
    print(f"This is your marks {M} and your grade is F")
else:
    print("I dont know what you enter ")
print("--- THANKS YOU ---")

#THIS IS ABIT WRONG 