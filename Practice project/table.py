
# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

num_people=input("How many people are in your group : ")
num_people=int(num_people)
if(num_people < 8):
    print(f"We have a table for {num_people}")
else:
    print("Sorry you have to wait")