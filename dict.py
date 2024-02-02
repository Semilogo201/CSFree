#working on dictionaries
mdict = {"maths":78, "science":96}
#using the key to get the value in it 
print(mdict["science"])
print(mdict["maths"])
print(mdict.get("science"))

#using a for loop to get the menbers of a dictionary
#1
for i in mdict:
    #print(i)
    print(mdict[i])
#2  To get the subjects 
    for subject in mdict.keys():
        print(subject)
#3 To get the values
    for subject in mdict.values():
          print(subject) 
#4  items will return both the key and value as tuple
    for subject in mdict.items():
        print(subject)
#5
    for subject, score in mdict.items():
        print(subject)
        print(f"Subject = {subject} and Score = {score}")
         #how to update contents of our dictionary
        dict = {"a":56, "b":67}
        dict["c"] = 89
        print(dict)
        dict["a"] = 100
        print(dict)
        