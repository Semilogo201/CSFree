#!/usr/bin/python3
#Creating user defined fxn
name = "Owolabi Oluwasemilogo"
yob = 1956
age = 2024 - yob

# print(f"{name}, you are {age} years old")

name = "Owolabi Oluwadamilola"
yob = 1986
age = 2024 - yob

print(f"{name}, you are {age} years old")
#creating a user def function of the above
def age_calculator(name, yob, current_year) :#parameters(placeholders)
    name = "Owolabi Oluwasemilogo"
yob = 1956
#age = current_year - yob
print(f"{name}, you are {age} years old")
#calling the function(parameters to the function is ())
#They are called positional arguement 
age_calculator("Owolabi Oluwasemilogo", 1986, 2024)#arguements(values)
age_calculator("Kelly Angela", 1982, 2024)#arguements(values)
age_calculator("Rapheal Effiong", 1946, 2019)#arguements(values)

age_calculator(2019, 1946, "Rapheal Effiong")#The output will be incorrect
#calling the function using keyword arguement
age_calculator(name="Owolabi Oluwasemilogo", yob=1986, current_year=2024)