// https://leetcode.com/problems/zigzag-conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
         return s

        lists = [''] * numRows
        index, step = 0, 1
        for char in s:
            lists[index] += char
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return ''.join(lists)   
        