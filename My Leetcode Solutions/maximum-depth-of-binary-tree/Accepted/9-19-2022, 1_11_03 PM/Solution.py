// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    BiggestDepth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        def depth(root, dep):
            if not root:
                return
            dep += 1
            if dep > self.BiggestDepth: self.BiggestDepth = dep
            if not root.left and not root.right:
                return
            
            depth(root.left, dep)
            depth(root.right, dep)
        depth(root, 0)
        
        return self.BiggestDepth