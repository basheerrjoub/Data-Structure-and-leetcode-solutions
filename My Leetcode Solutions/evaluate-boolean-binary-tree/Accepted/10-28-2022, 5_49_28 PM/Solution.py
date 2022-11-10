// https://leetcode.com/problems/evaluate-boolean-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        
        
        
        def do(root):
            
            if not root.left and not root.right:
                return root
            if root.left.val == 0 and root.right.val == 1:
                if root.val == 2:
                    return TreeNode(1)
                else:
                    return TreeNode(0)
            elif root.left.val == 1 and root.right.val == 0:
                if root.val == 2:
                    return TreeNode(1)
                else:
                    return TreeNode(0)
            elif root.left.val == 1 and root.right.val == 1:
                return TreeNode(1)
            elif root.left.val == 0 and root.right.val == 0:
                return TreeNode(0)
            
            root.left = do(root.left)
            root.right = do(root.right)
            return do(root)
        
        return (do(root).val)
            
        
            
                