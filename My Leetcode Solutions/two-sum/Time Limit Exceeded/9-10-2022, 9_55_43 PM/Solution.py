// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = []
        enumerate
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if(num1 + num2) == target and i != j:
                    array.append(i)
                    array.append(j)
                    return array
                
        
        