// https://leetcode.com/problems/shuffle-string

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        newString = ""
        lis = [0] * len(s)
        for i in range(len(s)):
            lis[indices[i]] = s[i]
        return newString.join(lis)