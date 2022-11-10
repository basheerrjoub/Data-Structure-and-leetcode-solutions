// https://leetcode.com/problems/root-equals-sum-of-children

class Solution(object):
    def checkTree(self, root):

        return not sum([root.left.val, root.right.val, -root.val])