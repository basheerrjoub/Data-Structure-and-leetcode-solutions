// https://leetcode.com/problems/climbing-stairs

class Solution(object):
    times = 0
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def climb(n):
            if n < 0:
                return
            if n == 0:
                self.times +=1
                return
            climb(n-2)
            climb(n-1)
        climb(n)
        return self.times