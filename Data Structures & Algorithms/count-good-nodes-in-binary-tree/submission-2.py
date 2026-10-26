# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cmax = root.val
        self.res = []

        def check_v(root, cmax):
            if not root:
                return

            if root.val >= cmax:
                self.res.append(root.val)

            cmax = max(cmax, root.val)

            check_v(root.left, cmax)
            check_v(root.right, cmax)

        check_v(root, cmax)
        return len(self.res)

            
            
        