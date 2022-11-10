// https://leetcode.com/problems/split-a-string-in-balanced-strings

class Solution(object):
    def balancedStringSplit(self, s):

        
        
        count = words = 0        
        for char in s:
            if char == "R": count += 1
            else: 
                count -= 1
            if count == 0:  words += 1
        
        return words
    
        