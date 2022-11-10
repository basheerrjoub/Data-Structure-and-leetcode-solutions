// https://leetcode.com/problems/decode-the-message

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        code = {}
        i = 97
        for char in key:
            if char not in code and char != " ":
                code[char] = chr(i)
                i += 1
        
        retMsg = ""
        for char in message:
            if char != " ":
                retMsg += code[char]
            else:
                retMsg += " "
        return retMsg