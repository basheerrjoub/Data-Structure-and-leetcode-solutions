// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        
        for first in range(len(nums)):
            for second in range(first+1,len(nums)):
                for third in range(second+1,len(nums)):
                    if nums[first] + nums[second] + nums[third] == 0:
                        ls = sorted([nums[first], nums[second], nums[third]])
                        if ls not in rList:
                            rList.append(ls)
        
        return rList
                        

        
            
            
        