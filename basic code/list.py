#Here we will learn list 
my_info= ["Sujal", 38 , "C" , "CSE"]
print(my_info)

#we can also access element as we want

print(my_info[0])

#we can also use string method 

print(my_info[0].upper())

#using indivdiual values of the list

info= f"Here is my info {my_info[0].upper()}, and my brach is {my_info[3]}"
print(info)

my_info.append("messi")
print(my_info)

my_info[1]= 7
print(my_info)

my_info.insert(0,"Ronaldo")
print(my_info)

del my_info[1]
print(my_info)

x=my_info.pop(1)
print(x)

y=my_info.pop()
print(y)