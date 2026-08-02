#this code print your current age
def age():
    current_year = int(input("Enter the current year :"))
    birth_year = int(input("Enter the birth  year :"))

    your_age = abs(current_year - birth_year)
    print(f"This is your age :{your_age}") 
    
    #abs is used to print the number always positive 


age()