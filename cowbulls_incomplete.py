'''
    Name: Shafaq Mandha 
    MISIS: M00914211
    Module: PDE1130
    SOB no. 31
'''
import random

cowbullcount=[] # declaring an empy list
def compare_numbers(number, user_guess):
    ## your code here
    current = 0 #Intializing the variables first
    cows = 0
    bulls = 0
    for i in user_guess:
        if i in number:
            cows+=1
            if number[current]==i:
                bulls+1
        else:
            current+=1
    cowbullcount=[cows,bulls]
    return cowbullcount # Changed "cowbull" to "cowbullcount". 

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print(number) # Changed "print number" to "print(number)"

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #Changed "raw_input" to "input"
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number)) #Added guesses before the "!" mark.
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
