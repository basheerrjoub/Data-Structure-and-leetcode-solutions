// https://leetcode.com/problems/concatenation-of-array

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for i in range(len(nums)):
            array.insert(i, nums[i])
            array.insert(len(nums)+i, nums[i])
        
        return array