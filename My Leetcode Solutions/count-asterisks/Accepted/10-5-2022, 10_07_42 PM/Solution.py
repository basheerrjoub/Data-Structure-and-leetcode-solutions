// https://leetcode.com/problems/count-asterisks

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        skip = 0
        count = 0
        for char in s:
            if char == "|" and skip == 0:
                skip = 1
            elif char == "|" and skip == 1:
                skip = 0
                continue
            elif char == "*" and skip == 0:
                count += 1
        
        return count
                
        