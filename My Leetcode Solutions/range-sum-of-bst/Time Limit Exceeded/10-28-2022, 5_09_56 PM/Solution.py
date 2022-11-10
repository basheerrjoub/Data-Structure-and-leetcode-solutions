// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):

        
        def traverse(root):
            
            if not root: return 0
            if root.val > high:
                traverse(root.left)

            if root.val < low:
                traverse(root.right)
            
            s = 0
            if low <= root.val <= high:
                s = root.val
            return s + traverse(root.left) + traverse(root.right)
        
        return traverse(root)
        
            