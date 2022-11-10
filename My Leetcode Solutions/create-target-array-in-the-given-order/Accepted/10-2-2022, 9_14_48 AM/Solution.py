// https://leetcode.com/problems/create-target-array-in-the-given-order

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        
        newList = [None] * len(index)
        
        for i in range(len(index)):
            if newList[index[i]] is None:
                  newList[index[i]]  = nums[i]
            else:
                 newList = newList[:index[i]] + [nums[i]] + newList[index[i]:]
        
        return newList[:len(nums)]