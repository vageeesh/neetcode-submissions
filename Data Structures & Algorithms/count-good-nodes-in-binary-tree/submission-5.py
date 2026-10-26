# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cmax = root.val

        def check_v(root, cmax):
            if not root:
                return 0

            if root.val >= cmax:
                # self.res += 1
                res = 1
            else:
                res = 0

            cmax = max(cmax, root.val)

            res += check_v(root.left, cmax)
            res += check_v(root.right, cmax)

            return res

        res = check_v(root, cmax)
        return res

            
            
        