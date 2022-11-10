// https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = 0
        left = len(height) - 1
        area = 0
        biggestArea = 0
        while right != left:
            leftValue = height[left]
            rightValue = height[right]
            if rightValue > leftValue:
                area = leftValue * (left - right)
                left -= 1
            else:
                area = rightValue * (left - right)
                right +=1
            biggestArea = max(area, biggestArea)
        return biggestArea
        