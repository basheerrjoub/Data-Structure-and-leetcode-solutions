// https://leetcode.com/problems/build-array-from-permutation

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rList = []
        for i in nums:
            rList.append(nums[i])
        return rList 