// https://leetcode.com/problems/richest-customer-wealth

class Solution(object):
    def maximumWealth(self, accounts):

        
        return max(list(map(lambda x: sum(x), accounts)))
        