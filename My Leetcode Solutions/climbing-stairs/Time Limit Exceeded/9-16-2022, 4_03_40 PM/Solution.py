// https://leetcode.com/problems/climbing-stairs

class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def climb(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return climb(n-2) + climb(n-1)
        
        return climb(n)