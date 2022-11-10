// https://leetcode.com/problems/to-lower-case

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        rStr = ""
        for char in s:
            n = ord(char)
            if 64 < n < 91:
                rStr += chr(n + 32)
            else:
                rStr += char
        return rStr