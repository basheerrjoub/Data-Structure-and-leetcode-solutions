// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ml = 0
        for sen in sentences:
            space = 0
            for char in sen:
                if char == " ":
                    space += 1
            if space > ml:
                ml = space
        return ml + 1
        