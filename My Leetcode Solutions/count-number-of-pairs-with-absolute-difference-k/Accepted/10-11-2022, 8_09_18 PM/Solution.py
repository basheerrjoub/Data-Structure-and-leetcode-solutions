// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

class Solution(object):
    def countKDifference(self, nums, k):

        
        
        
        count = 0
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if abs(nums[i] - nums[j]) == k:
                    count +=1
                j+=1
            i+=1
        return count