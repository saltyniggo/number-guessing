#basic number guessing game
#computer chooses a random number
#user chooses a random number
#if those numbers are the same user wins
#-> the number shall only be in a given range

from random import randint

#variables for tje computers number and users guess
comp_num = ''
user_num = ''

#define how the game works
def num_guess():
    comp_num = randint(1, 100)
    user_num = input("which number do you choose: ")
    if comp_num == user_num:
        print("user wins!")
    else:
        print("computer wins")

#start the game
num_guess()