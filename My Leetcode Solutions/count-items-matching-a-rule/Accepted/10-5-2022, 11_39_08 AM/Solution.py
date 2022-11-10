// https://leetcode.com/problems/count-items-matching-a-rule

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        r = 0
        if ruleKey == "color": r = 1
        elif ruleKey == "name": r = 2
        
        count = 0
        for item in items:
            if item[r] == ruleValue:
                count += 1
        
        return count
        