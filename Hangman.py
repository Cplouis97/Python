#Hangman Style Game about me
import time
import sys
from time import sleep

def play_game(pgques, pgans):
    ansLength = len(pgans) # captures the length of the answer
    placeholder = []
    pgans = list(pgans)
    #print(pgans)
    gStrikes = 0 # counter variable
    endGame = 2 # How many tries does a player have
    letGuessed = ""

    for i in range(ansLength):
            placeholder.append("*") # adds underscores to the placeholder for aesthetics
    for j in range(ansLength):
        if pgans[j] == " ":
            placeholder[j] = " " #places a space in the placeholder if needed

    placeholder = "".join(placeholder)

    while gStrikes < endGame:
        print("\n" + pgques)
        print(placeholder) #prints the place holder so the player can see
        placeholder = list(placeholder) #creates an array
        letGuessed = input("\nEnter a Letter: ") #user enters a letter that is captured into the letGuessed variable

        foundLetter = False #boolean variable that changes to true if a letter is found

        for k in range(ansLength):
            if pgans[k].lower() == letGuessed.lower(): #compares the letter guessed with the letters in the answer array
                placeholder[k] = pgans[k] #if a letter is guessed correctly the letter in the answer is substituted into the placeholder
                #print("found letter") - Test to ensure that a a letter was found
                foundLetter = True #changes to true if letter guessed is present in the answer

        if not foundLetter:
            print("No Letters found") #prints if the letter the user enters is not found in the answer
            gStrikes += 1 #adds a strike if you guessed a letter that is not found in the answer

        if placeholder == pgans: #if the placeholder is equal to the answer array the user has guessed all the correct letters to end the game
            pgans = "".join(pgans) #rejoins the answer to form a string
            print("Great Job, You Win!!!!!")
            print("The answer was: " + pgans)
            exit() #exits the program

        placeholder = "".join(placeholder) #rejoins placeholder to be displayed appropriately as a string for the player

    if gStrikes == endGame: #if the player guesses incorrectly to many times the answer is displayed an the game ends
        pgans = "".join(pgans)
        print("\nSorry the answer was: " + pgans) #
        print("Better Luck Next Time!")

    #print(pgques)
    #print(pgans)
   # print(placeholder)

intro = "Hello World My Name is Carl!"
ans1 = ""
gAns = ["Cyber Security", "LeBron James", "Florida Atlantic University"] # array of answers for the game
gQues = ""
gAns1 = ""

for char in intro: # creates typing effect
    sleep(.23)
    sys.stdout.write(char)
    sys.stdout.flush()

sleep(1) # quick pause

print("\n\nAnd this is a Hangman Game About ME!\n")

ans1 = input("Want to Play? (y or n): ")
ans1 = ans1.lower() #changes the user's answer to lowercase

#print(ans1) test to ensure answer is lowercase
if ans1 == 'y': # if the user elects to play the following occurs
    print("Great!\n")
    print("1. What is Carl's Favorite Subject? ")
    print("2. Who is Carl's Favorite NBA player? ")
    print("3. What college does Carl go to? ")
    uOption = input("Choose an option to play (1-3): ")

    if uOption == '1':
        gQues = "What is Carl's Favorite Subject?"
        gAns1 = gAns[0]

    elif uOption == '2':
        gQues = "Who is Carl's Favorite NBA player?"
        gAns1 = gAns[1]

    elif uOption == '3':
        gQues = "What college does Carl go to?"
        gAns1 = gAns[2]
    else:
        print("Sorry Incorrect Entry")

    play_game(gQues, gAns1)



else: # if the user does not elect to play
    print("Aww Man ok, Have a Great Day!")


