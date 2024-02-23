#Randomisation and python lists
#if we want our prog to do different thgs each time, we use randomisationThey are majorly used in games because we want the outcome to be unpredictable
#for us to tap into the random module in python, we have to import it first

import random 
random_integer = random.randint(1, 10)
print(random_integer)

#random module in a python module. for a very long code, we can split the module into different functionality, each module doing a different things.
#how do we create our own modules
#0.00000 - 0.999999....
random_float = random.random()
print(random_float)
#expanding from 0-1 to 0-5, note: this excludes 1 and 5.
flo = random_float * 5
print(flo)

#for a love calculator, if it is random
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random
random_num = random.randint(0, 1)
if random_num == 0:
    print("Tails")

else:
    print("Heads")

#a list is what you will call a data structure.The index is not talking about the position but the offset or shift.
#names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
#to get the total num of items in the list
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
num_names = len(names)
#to gen random names betwn 0 and the last index
random_name = random.randint(0, num_names -1)
paying_persn = names[random_name]
print(paying_persn + " " + "is going to buy the meal today!")

#Creating a list of dirty dozen(index error)
dirty_dozen = ["strawberries", "spinach", "kale", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "potatoes"]

fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][1])

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
#map = [line1, line2, line3]
#print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) -1
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#In this exercise, you're given a 3x3 grid, and the user needs to input a position (e.g., A1, B2) to mark that position with an 'X' on the grid. Your task is to modify the code to update the grid based on the user's input and then print the updated grid.
grid = [
    ["⬜️", "⬜️", "⬜️"],
    ["⬜️", "⬜️", "⬜️"],
    ["⬜️", "⬜️", "⬜️"]
]

print("Welcome to the grid game, find the hidden item by marking its location with an 'X'. ")
position = input("Enter the position  (e.g., A1): ").upper()

for row in grid:
    print(" ".join(row))

#input rock, paper and scissors
import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer = random.randint(0, 2)
print(f"Computer chose: {computer}")

if user >= 3 or user < 0:
    print("You typed a wrong figure")
elif user == 0 and computer == 2:
    print("You win the game")
elif computer > user:
    print("You lose the game")
elif user == computer:
    print("It is a draw")
elif computer == 0 and user == 2:
    print("You lose") 
elif user > computer:
    print("you win")
