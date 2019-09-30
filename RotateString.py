print("------------------- Rotate String -------------------")
x = [] # array to hold rotated strings

y = input("Enter a word: ") #user will input a word they would like to rotate

sLength = len(y) # takes in the length of the string which will be used later

t=0 # counter variable for the while loop

#We want to have as many strings as there are charaters in the word
#This while loop will help facilitate the rotating and adding the strings to the array
while t < sLength:
    k = 1
    fLet = y[0] # copies the first letter of the string into this variable

    #The for loop rotates the letters in the string
    for i in range(sLength):
        y = list(y) #Strings can not be manipulated so the string the user entered is turned into an array


        if i == sLength -1: #to effectivel
            y[i] = fLet #replaces the last letter with the first letter that was copied earlier
        else:
            y[i] = y[k]

        k = k + 1
    y = "".join(y) #joins the charaters in the array to now form a string
    x.append(y) #adds the string to the array
    t = t +1 #incriments the counter variable for the while loop


print(x) # prints the entire array with the rotated strings




