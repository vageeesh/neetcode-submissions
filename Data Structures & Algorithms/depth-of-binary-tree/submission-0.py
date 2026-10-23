# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self, root, cdepth, maxdepth):
        cdepth = 0
        if not root:
            maxdepth = max(maxdepth, cdepth)
            return

        cdepth += 1

        self.find_depth(root.left, cdepth, maxdepth)
        self.find_depth(root.right, cdepth, maxdepth)

        return cdepth


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        return max(left, right)
        