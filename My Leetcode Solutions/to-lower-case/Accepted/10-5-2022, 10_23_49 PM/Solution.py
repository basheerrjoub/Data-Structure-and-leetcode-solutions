// https://leetcode.com/problems/to-lower-case

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            if 64 < ord(s[i]) < 91:
                s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]

        return s