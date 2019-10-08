def main():
    j = 1
    w = 1
    fAns = False
    nums = input("Enter Values Separated by a space: ") # user enters values
    nums = nums.split(" ") #Split here to remove the spaces from the users entry

    for l in range(len(nums)): #Each value in the array is then converted to an integer value
        nums[l] = int(nums[l])
    val1 = input("Enter Value: ") #Here the user enters a number which we are to find two values in the array that add up to that value
    val2 = len(nums) #length of the array is calculated to later be used within the for loop
    for i in range(val2): #loop to cycle through values within array
        j = w
        # print("Top j: " + str(j))
        for k in range(val2): # Another loop to add numbers in the array together
            if j == val2: #This will act as an error handler so the array does not go out of bounds
                break
            sum1 = nums[i] + nums[j]
            if sum1 == int(val1): #if we find two numbers that satifies the answer the boolean value becomes true
                # print("Answer found")
                fAns = True
                break
            j += 1 # the value j is incremented to cycle through array
        if fAns:
            break
        w += 1
    aIndex = [i, j] #Indicies of values that add up to the given number
    if fAns:
        print(aIndex)
    else:
        print("No Values in the array summed up to the given value")


if __name__ == '__main__':
    main()