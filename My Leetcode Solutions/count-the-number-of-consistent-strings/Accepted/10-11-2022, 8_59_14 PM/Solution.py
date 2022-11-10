// https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            count +=1
            for char in word:
                if char not in allowed:
                    count -=1
                    break
        return count