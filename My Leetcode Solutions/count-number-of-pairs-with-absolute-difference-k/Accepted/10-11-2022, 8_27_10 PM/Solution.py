// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

class Solution(object):
    def countKDifference(self, nums, k):

        
        
        
        save = {}
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] not in save:
                save[nums[i]] = 1
            else:
                save[nums[i]] += 1
            i += 1
        i = 0
        
        while i < len(nums):
            dif = (nums[i] - k)
            if dif in nums:
                count += save[dif]
            i+=1
        return count 