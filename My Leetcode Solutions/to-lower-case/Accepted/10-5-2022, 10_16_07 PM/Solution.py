// https://leetcode.com/problems/to-lower-case

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        rStr = ""
        for char in s:
            if 64 < ord(char) < 91:
                rStr += chr(ord(char) + 32)
            else:
                rStr += char
        return rStr