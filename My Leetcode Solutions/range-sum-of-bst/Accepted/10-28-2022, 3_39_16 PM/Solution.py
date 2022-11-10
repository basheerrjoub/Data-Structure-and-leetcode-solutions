// https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sum = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def traverse(root):
            
            if root:
                traverse(root.left)
                if low <= root.val <= high:
                    self.sum += root.val
                traverse(root.right)
        traverse(root)
        return self.sum
        
            