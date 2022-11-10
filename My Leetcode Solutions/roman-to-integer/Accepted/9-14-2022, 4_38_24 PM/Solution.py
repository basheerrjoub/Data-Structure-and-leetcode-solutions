// https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        i=0
        while i < len(s):
            if s[len(s) - i - 1] == "I":
                    number += 1
                
                    
            if s[len(s) - i - 1] == "V":
                if (len(s) - i - 1) == 0:
                    number += 5
                elif s[len(s) - i - 2] == "I":
                    number +=4
                    i +=1
                else:
                    number += 5
                    
            if s[len(s) - i - 1] == "X":
                if (len(s) - i - 1) == 0:
                    number += 10
                elif s[len(s) - i - 2] == "I":
                    number +=9
                    i +=1
                else:
                    number += 10
            if s[len(s) - i - 1] == "L":
                if (len(s) - i - 1) == 0:
                    number += 50
                elif s[len(s) - i - 2] == "X":
                    number +=40
                    i +=1
                else:
                    number += 50
                    
            if s[len(s) - i - 1] == "C":
                if (len(s) - i - 1) == 0:
                    number += 100
                elif s[len(s) - i - 2] == "X":
                    number +=90
                    i +=1
                else:
                    number += 100
                    
            if s[len(s) - i - 1] == "D":
                if (len(s) - i - 1) == 0:
                    number += 500
                elif s[len(s) - i - 2] == "C":
                    number +=400
                    i +=1
                else:
                    number += 500
                    
            if s[len(s) - i - 1] == "M":
                if (len(s) - i - 1) == 0:
                    number += 1000
                elif s[len(s) - i - 2] == "C":
                    number +=900
                    i +=1
                else:
                    number += 1000
            i +=1
        return number
            
            
                    
        