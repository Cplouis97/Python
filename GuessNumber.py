import random
from time import sleep


def main(x):
    num1 = random.randint(0,20)
    user_Guess = ""
    while user_Guess != num1:
        user_Guess = input("Guess a Number between 1 - 20: ")
        user_Guess = int(user_Guess)
        if user_Guess > num1:
            print("Lower!")
        elif user_Guess < num1:
            print("Higher!")

    print("Great job " + x + " you guessed it!")
    sleep(1.3)
    print("Thank you for playing!")
    sleep(1)



print("--------------- Guess a Number Game ---------------")
name = input("Enter your name please: ") # users name is entered for later use

if __name__ == '__main__':
    main(name)