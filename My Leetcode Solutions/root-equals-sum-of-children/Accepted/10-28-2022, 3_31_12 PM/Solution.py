// https://leetcode.com/problems/root-equals-sum-of-children

class Solution(object):
    def checkTree(self, root):

        return not (root.left.val + root.right.val - root.val)