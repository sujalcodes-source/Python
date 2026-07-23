gust_list=["Sujal","Messi","Ronaldo","Dembele","R9"]
print(f"You are invited to the party {gust_list}")

print(f"He can\' be at party {gust_list[1]}")

gust_list[1]= "Mbaape"
print(gust_list)

gust_list.insert(0,"Kaka")
gust_list.insert(3, "Vitiha")
gust_list.append("Saka")
del gust_list[7]
del gust_list[5]
print(gust_list)

gust_list.sort()
print(gust_list)
print(sorted(gust_list))

gust_list.reverse()
print(gust_list)

gust_list.reverse()
print(gust_list)

print(len(gust_list))
