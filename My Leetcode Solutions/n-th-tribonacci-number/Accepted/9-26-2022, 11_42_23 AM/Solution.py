// https://leetcode.com/problems/n-th-tribonacci-number

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        save = {}
        save[0] = 0
        save[1] = 1
        save[2] = 1
        def generate(n):
            
            if n in save:
                return save[n]
            else:
                res = generate(n-3) + generate(n-2) + generate(n-1)
                if res not in save:
                    save[n] = res
                return res
        return generate(n)