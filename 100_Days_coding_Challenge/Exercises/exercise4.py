# identity operators in python
t = 2
u = 2
print(t is u)
print(t == u)
print(id(t))
print(id(u))

#membership operator(in, not in)
s = 'owolabi oluwasemilogo'
print('owe' not in s)

#task 1
#bmi calculator
weight=int(input('Enter weight in kg: '))
height=float(input('Enter height in meter: '))

bmi=weight/height ** 2
print(int(bmi))