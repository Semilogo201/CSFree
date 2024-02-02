#two same element cannot be in a set
myset = {3, 4, 5, 6}
#element of a set is immutable but a set itself is mutable
print(myset)
#can add element to a set using the add method
#1 #operations (union, intersection, difference, symmetric_difference)
urset = {6, 8, 10, 12, 14, 16}
print(myset.union(urset))
#2
print(myset or urset)
#intersection(similarity)
print(myset.intersection(urset))
print(myset or urset)

#1 #difference
print(myset.difference(urset))
print(urset.difference(myset))

#2 another method
print(myset - urset)
print(urset - myset)

#symmetrical difference
myset.symmetric_difference(urset)
#converting a list to a set
mylist = [1, 2, 3, 4, 5]

#converting a list to a set
print(set(mylist))

#converting a list to a tuple
print(tuple(mylist))