// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        retList = []
        
        for i in range(len(boxes)):
            op = 0
            left = len(boxes) - 1 
            right = 0 
            while right < i:
                if boxes[right] == "1":
                    op += i - right
                right += 1  
                
            while left > i:
                if boxes[left] == "1":
                    op += left - i
                left -= 1
            retList.append(op)
        return retList
                    