// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        big = max(candies)
        newList = []
        for can in candies:
            if (can + extraCandies) >= big:
                newList.append(True)
            else:
                newList.append(False)
        return newList