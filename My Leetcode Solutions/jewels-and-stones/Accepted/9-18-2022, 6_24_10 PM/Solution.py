// https://leetcode.com/problems/jewels-and-stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        if not jewels or not stones:
            return 0
        jew = {}
        for char in jewels:
            jew[char] = 0
        
        for char in stones:
            if char in jew:
                jew[char] += 1
        sum = 0
        for char in jew:
            sum += jew[char]
        
        return sum