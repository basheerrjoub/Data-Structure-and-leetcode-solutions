// https://leetcode.com/problems/fibonacci-number

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cal = {}
        def generate(n):
            
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n in cal:
                return cal[n]
            else:
                res =  generate(n-1) + generate(n-2)
                if n not in cal:
                    cal[n] = res
                return res
        return generate(n)