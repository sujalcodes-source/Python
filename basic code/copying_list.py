# copying using slice
my_info= ["Sujal", 38 , "C" , "CSE"]
sujal_info = my_info[:]
print(f"This is sujal info{sujal_info}")

#copying using copy() function
sujal_info=my_info.copy()
print(sujal_info)