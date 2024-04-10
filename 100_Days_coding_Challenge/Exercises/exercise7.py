weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in meters: "))

bmi = round(weight/height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi} and you are normal.")  
elif bmi < 30:
    print(f"your bmi is {bmi} and you are overweight.")  
elif bmi < 35:
    print(f"your bmi is {bmi} and you are Obese.")  
else:
    print(f"your bmi is {bmi} and you are clinically obese.")  


#checking if a year is a leap year or not
year = int(input('Enter the year: '))

if year % 4 == 0:
    print("it's a leap year")