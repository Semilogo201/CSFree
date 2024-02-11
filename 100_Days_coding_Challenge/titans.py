#Write a program that takes a positive integer as input 
#determines whether it is a prime number. 
#Keep prompting the user until they enter a positive integer. 
#The program should print whether the entered number is prime or not.
#Remember, a prime number is a positive integer greater than 1 that is divisible only by 1 and itself.

def positive_int(prime_num):
    if prime_num <= 1:
        return False
    for i in range(2, int(prime_num**0.5) + 1):
        