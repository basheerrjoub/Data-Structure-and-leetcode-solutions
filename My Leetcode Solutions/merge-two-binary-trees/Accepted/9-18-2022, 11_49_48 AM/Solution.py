// https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, r1, r2):
        
        if r1 and r2:
            r = TreeNode(r1.val + r2.val)
            r.left = self.mergeTrees(r1.left, r2.left)
            r.right = self.mergeTrees(r1.right, r2.right)
            return r
        else:
            return r1 or r2