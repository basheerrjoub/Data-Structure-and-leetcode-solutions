// https://leetcode.com/problems/unique-morse-code-words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = {}
        mor = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        i = 97
        for string in mor:
            code[chr(i)] = string
            i += 1
            
        lis = []
        for word in words:
            string = ""
            for char in word:
                string += code[char]
            if string not in lis:
                lis.append(string)
            
       
        
        return len(lis)