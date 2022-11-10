// https://leetcode.com/problems/array-partition

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r = 0
        i = 0
        
        while i < len(nums):
            r += nums[i]
            i += 2
            
        return r