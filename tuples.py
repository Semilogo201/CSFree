#Study on tuple
scores = (80, 56, 87,40)
type(scores)
#Tuple indexing
print(scores[0])
print(scores[-1])
print(scores[:3])
#you cant del an element in a tuple
#del scores
print(len(scores))
my_score = (34, 23)
#You cant append in a tuple but you can add(using the concatination sign) two tuples together
print(scores + my_score)
print(scores + (67, 90))
#using a for loop to get the members of a tuple
result = (80, 76, 32, 90)
for result in result:
    print(result)

#swapping two numbers
a = 10
b = 20
#making b = 10 and a = 20
temp = a #temporal variable(temp) = 10
a = b # a = 20
b = temp #b = 10
#output swapped
print(a, b)
print(f"a = {a} and b = {b}")

#using tuples(output reswapped) to swap variables 
a, b = b, a
print(f"a = {a} and b = {b}")
