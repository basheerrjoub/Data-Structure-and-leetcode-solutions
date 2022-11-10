// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newList = []
        
        for cur in nums:
            count = 0
            for check in nums:
                if check < cur:
                    count += 1
            newList.append(count)
        return newList 
            