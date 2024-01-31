#common methods that can be used on the data structure LIST

names = ["emma", "yusuf", 24.5]
mylist = ["Tobi", "damy", 24.5]
num = [5, 10, 15, 20, 25, 30]
#checking the number of elements in a list
print(len(names))
print(len(mylist))
mynums = [1, 2, 3]
mynums.clear()
print(mynums)
print(mylist)
sorted(num)
print(num.append(20))
num.insert(0, 92)
num.extend([2, 3])
num.index(5)
new_num = num.copy()   
print(num)
num[5: 30: 2]
print(len(num))
names.pop()
print(names)
num.remove(15)
print(num)

#how to use conditionals and loops in D.str LIST
scores = [79, 68, 98, 55]

for score in scores:
    print(score)
    #for any score less than 90, add 10 marks
if score < 90:
     score = score + 10
    #or
score += 10
print(f"before: {scores}")
print(f"after: {scores}")

