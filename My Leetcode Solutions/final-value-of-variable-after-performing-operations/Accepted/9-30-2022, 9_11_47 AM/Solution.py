// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        add = "+"
        sub = "-"
        for op in operations:
            if add in op:
                x +=1
            elif sub in op:
                x -=1
                
        return x