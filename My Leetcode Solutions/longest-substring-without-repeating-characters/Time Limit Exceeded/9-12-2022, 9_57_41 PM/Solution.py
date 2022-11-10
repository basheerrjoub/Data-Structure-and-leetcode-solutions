// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        biggestLength = 0
        sub = ""
        lengthOfS = len(s)
        i=0
        while i < lengthOfS:
            char = s[i]
            if char not in sub: #dv
                sub += char
                length += 1
                if length > biggestLength:
                    biggestLength = length
                i+=1
            else:
                i = s.find(char) + 1
                sub = ""
                sub += char
                length = 1
        return biggestLength
                
            
        
        