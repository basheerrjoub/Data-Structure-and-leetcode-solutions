// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = []
    
        for indexofNum1,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums[indexofNum1:]:
                indexofNum2 = nums.index(num2)
                if indexofNum2 != indexofNum1:
                    array.append(indexofNum1)
                    array.append(indexofNum2)
                    return array                                                                                                                                       
                
        
        