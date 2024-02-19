# program to generate a random number and tell the user to guess
from random import randint
random_num = randint(1,10)
guessed_number = 3
if guessed_number == random_num:
    print("You are very correct")
else:
    print("oops, try again! The correct number is", random_num)