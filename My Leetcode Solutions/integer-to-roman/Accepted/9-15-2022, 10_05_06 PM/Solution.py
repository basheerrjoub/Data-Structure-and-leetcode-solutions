// https://leetcode.com/problems/integer-to-roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        string = ""
        chunk = 0
        dig = 1
        string = ""
        chunk = 0
        dig = 0
        while num > 0:
            chunk = num % 10
            num = num // 10
            dig += 1
            if dig == 1:
                while chunk != 0:
                    if chunk == 9:
                        string = "IX" + string
                        chunk -= 9
                    elif chunk == 5:
                        string = "V" + string
                        chunk -= 5
                    elif chunk == 4:
                        string = "IV" + string
                        chunk -= 4
                    else:
                        string = "I" + string
                        chunk -=1
                continue

            if dig == 2:
                while chunk != 0:
                    if chunk == 9:
                        string = "XC" + string
                        chunk -= 9
                    elif chunk == 5:
                        string = "L" + string
                        chunk -= 5
                    elif chunk == 4:
                        string = "XL" + string
                        chunk -= 4
                    else:
                        string = "X" + string
                        chunk -=1
                continue
            if dig == 3:
                while chunk != 0:
                    if chunk == 9:
                        string = "CM" + string
                        chunk -= 9
                    elif chunk == 5:
                        string = "D" + string
                        chunk -= 5
                    elif chunk == 4:
                        string = "CD" + string
                        chunk -= 4
                    else:
                        string = "C" + string
                        chunk -=1
                continue
            if dig == 4:
                while chunk != 0:
                    string = "M" + string
                    chunk -=1

        return string
                
            