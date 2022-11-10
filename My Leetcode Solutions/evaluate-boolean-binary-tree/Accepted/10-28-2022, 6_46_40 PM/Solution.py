// https://leetcode.com/problems/evaluate-boolean-binary-tree

class Solution(object):
    def evaluateTree(self, root):
        
        
        
        def do(root):
            
            if root.val == 2:
                left = do(root.left)
                right = do(root.right)
                return TreeNode(left.val or right.val)
            
            elif root.val == 3:
                left = do(root.left)
                right = do(root.right)
                return TreeNode(left.val and right.val)
            else:
                return TreeNode(root.val)

        
        return do(root).val