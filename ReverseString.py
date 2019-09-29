def reverse(x):
    sLength = len(x)
    placeholder = list(x)
    sLength = sLength -1
    i = 0
    #placeholder = list(placeholder)

    while sLength > - 1:
        placeholder[i] = x[sLength]
        i = i +1
        sLength = sLength - 1
    rStr = "".join(placeholder)
    return rStr

print("----------Reverse String APP----------")
y = input("Enter A String: ")

fStr = reverse(y)

print("Your original String was: " + y + "\nYour reversed string is: "  + fStr)

