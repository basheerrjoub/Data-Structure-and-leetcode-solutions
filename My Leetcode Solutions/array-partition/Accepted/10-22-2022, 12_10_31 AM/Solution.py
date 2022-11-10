// https://leetcode.com/problems/array-partition

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        r = 0
        
        for i in range(0, len(nums), 2):
            r += nums[i]
            
        return r