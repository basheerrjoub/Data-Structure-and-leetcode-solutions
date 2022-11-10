// https://leetcode.com/problems/increasing-decreasing-string

class Solution(object):
    def sortString(self, s):

        newStr = ""
        s = sorted(s)
        while len(s):
            point = "A"
            i = 0
            while i < len(s):
                if s[i] > point:
                    newStr += s[i]
                    point = s[i]
                    s = s[:i] + s[i+1:]
                    continue
                i += 1
                
            point = "{"
            i = len(s) - 1
            while i  >= 0:
                if s[i]  < point:
                    newStr += s[i]
                    point = s[i]
                    s = s[:i] + s[i+1:]
                i -= 1
        return newStr
        