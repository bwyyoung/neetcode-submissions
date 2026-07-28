# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def get_depth(self,  root: Optional[TreeNode], current: int):       
        if not root:
            return current
        current += 1
        cur_left = self.get_depth(root.left, current)
        cur_right = self.get_depth(root.right, current)
        return max(cur_left, cur_right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current = 0

        return self.get_depth(root, current)
        