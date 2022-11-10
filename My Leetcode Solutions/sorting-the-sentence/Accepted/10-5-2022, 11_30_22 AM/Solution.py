// https://leetcode.com/problems/sorting-the-sentence

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        save = {}
        newStr = s.split()
        for sen in newStr:
            save[int(sen[-1])] = sen[:-1]
        retStr = ""
        for i in range(1, len(newStr)+1):
            retStr += save[i] + " "
        
        return retStr[:-1]
        