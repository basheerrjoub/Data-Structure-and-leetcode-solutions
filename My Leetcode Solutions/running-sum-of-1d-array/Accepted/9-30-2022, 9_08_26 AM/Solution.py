// https://leetcode.com/problems/running-sum-of-1d-array

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rList = []
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            rList.append(runSum)
        return rList