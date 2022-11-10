// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        depth = 0
        for char in s:
            if char == "(":
                stack.append("(")
                depth = len(stack) if depth < len(stack) else depth
            elif char == ")":
                stack = stack[1:]
        return depth