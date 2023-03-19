def two_numbers(nums=[], target=0):
    nums_length = len(nums)
    nums_hash = {}

    for i in range(nums_length):
        num = nums[i]
        complement = target - num
    
        if complement in nums_hash:
            return ( i, nums_hash[complement] )
        else:
            nums_hash[num] = i
