#round () function
print(round(11.5))
print(round(12.5))
print(round(665, -1))
print(round(675, -1))
print(round(-8/3))
print(round(-1.5))

#exercise
#to find out how many days, weeks, months we have left if we live until 90 years old
age = int(input("What is your age: "))
years_left = 90 - age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print(days_left)
print(months_left)
print(weeks_left)
print(f"We have {years_left} years left, {months_left} months left, {weeks_left} weeks left and {days_left} days left")