// https://leetcode.com/problems/di-string-match

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lis = []
        save = collections.deque()
        for i in range(len(s)+1):
            save.append(i)
        
        for i in range(len(s)):
            if s[i] == "D":
                lis.append(save.pop())
            elif s[i] == "I":
                lis.append(save.popleft())
        
        lis.append(save.pop())
        return lis