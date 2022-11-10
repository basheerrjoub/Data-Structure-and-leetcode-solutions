// https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, r, n):
        
        if r and n:
            r.val = r.val + n.val
            r.left = self.mergeTrees(r.left, n.left)
            r.right = self.mergeTrees(r.right, n.right)
            return r
        else:
            return r or n