// https://leetcode.com/problems/richest-customer-wealth

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = map(lambda x: sum(x), accounts)
        
        return max(list(result))
        