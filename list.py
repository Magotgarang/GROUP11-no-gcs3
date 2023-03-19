def two_sum(nums, target):
    #create empty dictionary
    complements = {}

    # Loop through the numbers list
    for i, num in enumerate(nums):
        if target - num in complements:
            print(complements[target - num], i)
        complements[num] = i

    print("none")


# edit the values below to test the function
nums = [3, 2, 4, 1]
target = 5
two_sum(nums, target)
