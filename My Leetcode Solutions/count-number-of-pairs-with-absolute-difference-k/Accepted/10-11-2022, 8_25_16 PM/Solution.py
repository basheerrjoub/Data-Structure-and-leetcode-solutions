// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

class Solution(object):
    def countKDifference(self, nums, k):

        
        
        
        save = {}
        count = 0
        
        for num in nums:
            if num not in save:
                save[num] = 1
            else:
                save[num] += 1
        for num in nums:
            dif = (num - k)
            if dif in nums:
                count += save[dif]
        return count 