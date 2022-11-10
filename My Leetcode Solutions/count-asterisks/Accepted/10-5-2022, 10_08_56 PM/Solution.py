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
            if skip == 0 and char == "|":
                skip = 1
            elif skip == 1 and char == "|":
                skip = 0
                continue
            elif skip == 0 and char == "*":
                count += 1
        
        return count
                
        