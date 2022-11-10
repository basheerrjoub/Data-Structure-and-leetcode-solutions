// https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        rList = []
        rList.append([1])
        rList.append([1,1])
        for i in range(2,numRows):
            ls = []
            ls.append(1)
            for j in range(1,i):
                ls.append(rList[i-1][j-1] + rList[i-1][j])
            ls.append(1)
            rList.append(ls)
        return rList