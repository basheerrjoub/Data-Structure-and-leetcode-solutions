// https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = str(x)
        if number[0] == "-":
            return False
        revNumber = ""
        for i in range(len(number)):
            revNumber += number[len(number) - i - 1]
        
        intNumber = int(revNumber)
        if x == intNumber:
            return True
        else:
            return False
        