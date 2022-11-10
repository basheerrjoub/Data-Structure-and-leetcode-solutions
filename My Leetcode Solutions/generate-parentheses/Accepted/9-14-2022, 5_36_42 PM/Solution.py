// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        right, left, answer = n,n,[]
        
        def generate(left, right, str, answer):
            if right < left:
                return
            if right == 0 and left == 0:
                answer.append(str)
                return
            if left != 0:
                generate(left-1, right, str+"(", answer)
            if right != 0:
                generate(left, right-1, str+")", answer)
        generate(left, right, "", answer)
        return answer



