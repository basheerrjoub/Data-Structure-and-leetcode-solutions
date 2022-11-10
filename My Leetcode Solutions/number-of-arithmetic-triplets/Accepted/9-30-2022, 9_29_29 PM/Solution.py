// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        
        count = 0
        save = {}
        for i in range(len(nums)):
            if nums[i] + diff in nums[i+1:]:
                save[nums[i]] = nums[i] + diff
                
        for key, value in save.iteritems():
            if value in save:
                count +=1
        return count
                