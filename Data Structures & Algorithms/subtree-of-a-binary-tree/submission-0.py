# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def checkSubRoot(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot or not node:
            if not subRoot and not node:
                return True
            return False
        if node.val != subRoot.val:
            return False
        
        return (self.checkSubRoot(node.left, subRoot.left) and self.checkSubRoot(node.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        if self.checkSubRoot(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False
        