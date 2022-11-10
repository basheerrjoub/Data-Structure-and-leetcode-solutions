// https://leetcode.com/problems/smallest-even-multiple

class Solution(object):
    def smallestEvenMultiple(self, n):

        
        if n & 1:
            return n + n
        return n