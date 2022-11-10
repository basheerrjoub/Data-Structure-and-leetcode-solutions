// https://leetcode.com/problems/shuffle-the-array

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        rList = []
        
        for i in range(n):
            rList.append(nums[i])
            rList.append(nums[i+n])
        return rList