def sort_and_search(nums, target):
    nums_length = len(nums)
    # Sort the array
    nums.sort()
    
    # Search for the value
    # Using binary search method
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target > nums[mid]:
            start = mid + 1

        elif target < nums[mid]:
            end = mid - 1

        else:
            return mid

    return start
