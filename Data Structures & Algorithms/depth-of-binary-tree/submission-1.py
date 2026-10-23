# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self, root):
        self.max_depth = 0

        def rec_dept(root, cdepth):
            if not root:
                return 0

            cdepth += 1
            self.max_depth = max(self.max_depth, cdepth)

            rec_dept(root.left, cdepth)
            rec_dept(root.right, cdepth)

        rec_dept(root, 0)

        return self.max_depth
        


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.find_depth(root)
        