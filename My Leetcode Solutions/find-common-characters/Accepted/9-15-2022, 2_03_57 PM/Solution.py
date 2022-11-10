// https://leetcode.com/problems/find-common-characters

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = words[:]
        rlist = []
        char = ""
        counter = 0
        for i in range(len(words[0])):
            char += words[0][i]
            for j in range(len(words)):
                if i >= len(words[j]):
                    return rlist
                
                if char in words[j]:
                    counter += 1
                    words[j] =  words[j].replace(words[j][words[j].find(char)], "0", 1)
                   
            if counter == len(words):
                rlist.append(char)
                
            counter = 0
            char = ""
            
        return  rlist
        