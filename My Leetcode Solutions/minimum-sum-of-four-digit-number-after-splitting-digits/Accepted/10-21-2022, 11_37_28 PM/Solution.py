// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        strNum = str(num)
        lisNum = list(strNum)
        num1 = ""
        num2 = ""
        lisNum.sort()
        for i in range(0,len(lisNum)-1,2):
            num1 += lisNum[i]
            num2 += lisNum[i+1]

            
        return int(num1) + int(num2)