// https://leetcode.com/problems/number-of-good-pairs

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        out = 0
        for num in nums:
            if not freq.get(num):
                freq[num] = 1
            else:
                freq[num] +=1
        for num in freq:
            num = freq[num]
            out += num * (num -1) // 2
        return out
            
        