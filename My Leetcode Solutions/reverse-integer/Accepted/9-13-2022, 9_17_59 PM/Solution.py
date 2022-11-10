// https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        newNumber = ""
        if x < 0:
            newNumber += "-"
        number = str(abs(x))

        for i in range(len(number)):
            newNumber += number[len(number) - 1 -  i]

        returnNumber = int(newNumber)
        if returnNumber > pow(2, 31) - 1 or returnNumber < - pow(2,31) - 1:
            return 0
        return returnNumber                                                    
