def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    #Binary Search
    left = 0
    right = len(nums)-1
    while left <= right:
        number = (left+right) // 2
        if target > nums[number]:
            left = number+1
        elif target < nums[number]:
            right = number-1
        elif target == nums[number]:
            return number
        elif left == right:
            break
    if target > nums[number]:
        return number+1
    else:
        return number
print (searchInsert([1,3,5,6], 2))