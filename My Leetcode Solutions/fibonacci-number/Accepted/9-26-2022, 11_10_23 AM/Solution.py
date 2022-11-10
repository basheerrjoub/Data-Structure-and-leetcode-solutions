// https://leetcode.com/problems/fibonacci-number

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cal = {}
        cal[0] = 0
        cal[1] = 1
        def generate(n):
            
            if n in cal:
                return cal[n]
            else:
                res =  generate(n-1) + generate(n-2)
                if n not in cal:
                    cal[n] = res
                return res
        return generate(n)