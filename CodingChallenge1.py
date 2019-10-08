def main():
    j = 1
    w = 1
    fAns = False
    nums = input("Enter Values: ")
    nums = nums.split(" ")
    for l in range(len(nums)):
        nums[l] = int(nums[l])
    val1 = input("Enter Value: ")
    val2 = len(nums)
    print(nums)
    for i in range(val2):
        j = w
        # print("Top j: " + str(j))
        for k in range(val2):
            if j == val2:
                break
            sum1 = nums[i] + nums[j]
            if sum1 == int(val1):
                # print("Answer found")
                fAns = True
                break
            j += 1
        if fAns:
            break
        w += 1
    aIndex = [i, j]
    if fAns:
        print(aIndex)
    else:
        print("No Values in the array summed up to the given value")


if __name__ == '__main__':
    main()