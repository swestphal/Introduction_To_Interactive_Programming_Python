# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global nr_of_tries
    range100()
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global nr_of_guesses
    global nr_of_tries
    nr_of_guesses = 7
    nr_of_tries = 1
    secret_number = random.randrange(0, 101)
    print "\nNew secret number between 0 and 100 generated\nPlease start to guess\n"
    print "It remains",nr_of_guesses,"guesses" 
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global nr_of_guesses 
    global nr_of_tries
    nr_of_guesses = 10
    nr_of_tries = 1
    secret_number = random.randrange(0, 1001)
    print "\nNew secret number between 0 and 1000 generated\nPlease start to guess\n"
    print "It remains", nr_of_guesses, "guesses"
    pass
    

def input_guess(guess):
    # main game logic goes here 
    global selected
    global nr_of_guesses 
    global nr_of_tries
    remaining_guesses = nr_of_guesses - nr_of_tries
    print "\nGuess was", guess
    guess = int(guess) 
    if ((guess > secret_number) or (guess < secret_number)):
        print "Number of remaining guesses", remaining_guesses
        if  (guess > secret_number):
            print "Lower"
        elif (guess < secret_number):
            print "Higher"
        
        nr_of_tries += 1
        if (remaining_guesses == 0):
            print "\nYou have run out of tries.\n"
            print "The secret number was :", secret_number
        
    elif (guess == secret_number):
        print "Correct\n"
      
    if ((remaining_guesses == 0) or (guess == secret_number)):
        print "New game starts with a range of 0-100\n"
        print "Or select new range with buttons\n"
        range100()
    pass

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 400, 400)

# register event handlers for control elements and start frame
frame.add_label('Welcome to \"Guess the number\"')
frame.add_label('')
frame.add_label('Please press button to select a range')
frame.add_label('')
frame.add_label('If no button is pressed, the game')
frame.add_label('starts with a number between 0-100')
frame.add_label('')
frame.add_button("Range is [0,100]", range100, 200)
frame.add_button("Range is [0,1000]", range1000, 200)
frame.add_label('')
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


