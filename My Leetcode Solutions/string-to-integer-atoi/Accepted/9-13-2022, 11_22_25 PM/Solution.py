// https://leetcode.com/problems/string-to-integer-atoi

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ls = list(s.strip())
        if len(ls) == 0:
          return 0
        #Choosing the sign
        sign = -1 if ls[0] == "-" else 1


        if ls[0] in "-+":
           del ls[0]
        number = 0
        i = 0
        for i in range(len(ls)):
            if ls[i].isdigit():
                number = number * 10 + ord(ls[i]) - ord('0')
            elif ls[i] == ".":
                return number
            elif number > 0:
                break
            else: return 0
        number *= sign
        if number > 2**31 -1:
            return 2**31 -1
        if number < -2**31:
            return -2**31
        return number