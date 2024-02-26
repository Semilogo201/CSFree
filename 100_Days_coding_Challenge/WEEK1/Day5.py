# #the concept of loops
# #the for loop
# fruits = ['apple', 'Peach', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie") #this works inside the for loop
# print(fruit + " pie") #not that indentation is very important, this is outside the for loop

#A program that works out the average heights of students
student_heights  = input().split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    theight = 0
    for height in student_heights:
        theight += height
        print(f"total height = {theight}")
        #or
        numstudent = 0
        for student in student_heights:
            numstudent += 1
            print(f"number of student = {numstudent}")

            averageH = round(theight/numstudent)
            print(f"average height = {averageH}")