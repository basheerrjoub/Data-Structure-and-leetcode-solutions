// https://leetcode.com/problems/decompress-run-length-encoded-list

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newList = []
        i = 0
        while i in range(len(nums)):
            for j in range(nums[i]):
                newList.append(nums[i+1])
            i += 2
        return newList