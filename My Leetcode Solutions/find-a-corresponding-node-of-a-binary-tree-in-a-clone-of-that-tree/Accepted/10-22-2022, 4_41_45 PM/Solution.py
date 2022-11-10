// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        node, clon = original, cloned 
        stack = []
        
        
        while node is not None:
            if node.val == target.val == clon.val:
                return clon
                
            if node.left:
                stack.append(node.left)
                stack.append(clon.left)
                
            if node.right:
                stack.append(node.right)
                stack.append(clon.right)
            clon = stack.pop()
            node = stack.pop()
            
            
            
        
            