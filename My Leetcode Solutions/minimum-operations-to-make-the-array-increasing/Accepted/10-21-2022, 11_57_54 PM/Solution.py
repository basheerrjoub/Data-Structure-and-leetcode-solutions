// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        for i in range(len(nums)-1):
            dif = nums[i+1] - nums[i]
            if dif > 0:
                continue
            else:
                count += -dif + 1
                nums[i+1] += -dif + 1
        return count