#list sum:
#create a function that takes a list of number as input and 2. returns the sum of element in the list. give the necassary step in solving this question
#pseudocode

#define our function
# function takes in a list
#add the elements of the list
#list of numbers
 #solution
#refactorization(checking for time complexity)
#O(n) the amt of the element is the amount of time it will have to run that means it will run 10times, n = 10.
def sum_numbers(lst=None):
    #the none is a default parameter and if we pass another thing, it will overwrite none.
    #sum = 0
    #total = 0
    total = sum(lst)
    return total
    #for i in lst:
        #total += i
        #sum += i
        # sum = sum + i
        #the diff betn return and print is for return, just cast it to a variable but for print, just call the initial variable assigned and thats all
    #return sum
    #print(lst)
try:
    total = (sum_numbers([1,2,3,4,5,6,7,8,9,10]))
    print(total)
