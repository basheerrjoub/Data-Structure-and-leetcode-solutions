// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        pos = []
        neg = []
        zero = 0
        for num in nums:
            if num >= 0:
                pos.append(num)
                if num == 0:
                    zero += 1
            elif num < 0:
                neg.append(num)
            
                
        for first in range(len(pos)):
            for second in range(first+1, len(pos)):
                for third in range(len(neg)):
                    if pos[first] + pos[second] + neg[third] == 0:
                        ls = sorted([pos[first], pos[second], neg[third]])
                        if ls not in rList:
                            rList.append(ls)
        for first in range(len(neg)):
            for second in range(first+1, len(neg)):
                for third in range(len(pos)):
                    if neg[first] + neg[second] + pos[third] == 0:
                        ls = sorted([neg[first], neg[second], pos[third]])
                        if ls not in rList:
                            rList.append(ls)
        if zero >= 3:
            rList.append([0,0,0])

        
        return rList
                        

        
            
            
        