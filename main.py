# This is a basic number guessing game where the computer chooses a random number
# and the user has to guess what that number is.
# The number can only be within a given range (1-100 in this case)

# First we import randint for the random number of the computer
from random import randint

# Then we initialize the variables for the computers and users number and also the play again variable
play_again = '1'
comp_num = ''
user_num = ''

# We then start the while loop of the game
while play_again == '1':
    # First the computers number gets randomized and the user chooses his number
    comp_num = randint(1, 50)
    user_num = input("which number do you choose?: ")
    # If the numbers are the same the user wins
    if comp_num == user_num:
        print("user wins!")
        # Then the user gets asked to play another time
        print("you want to play another time?:")
        again = input("yes or no? ")
        if again == 'no' or again == 'n':
            print("alright, see you soon!")
            play_again = '0'
    # If the numbers arent the same the computer wins
    else:
        print("computer wins")
        print("you want to play another time?:")
        again = input("yes or no? ")
        if again == 'no' or again == 'n':
            print("alright, see you soon!")
            play_again = ''
