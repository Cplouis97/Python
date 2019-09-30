def reverse(x):
    sLength = len(x)
    placeholder = list(x) #Used to create an array
    sLength = sLength -1 #will be used later to access a character at a specific index
    i = 0
    #placeholder = list(placeholder)

    while sLength > - 1:
        # this is where the rotation takes place
        placeholder[i] = x[sLength]

        #counter variables
        i = i +1
        sLength = sLength - 1

    rStr = "".join(placeholder)#joins the characters together to form a string
    return rStr #Returns the reversed string

print("----------Reverse String APP----------")
y = input("Enter A String: ") #user enters a string that they want to reverse

fStr = reverse(y) #Captures the returned string from the function

print("Your original String was: " + y + "\nYour reversed string is: "  + fStr) #Prints the original String and the Newly reversed string

