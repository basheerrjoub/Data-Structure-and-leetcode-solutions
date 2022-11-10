// https://leetcode.com/problems/di-string-match

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lis = []
        p1 = len(s)
        p2 = 0
        
        for i in range(len(s)):
            if s[i] == "D":
                lis.append(p1)
                p1 -=1
            elif s[i] == "I":
                lis.append(p2)
                p2 +=1
        
        lis.append(p1)
        return lis