# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalenced = True

        def find_height(root):
            if not root:
                return 0
            
            lh = find_height(root.left)
            rh = find_height(root.right)

            if ((rh-lh) > 1) or ((lh-rh) > 1):
                self.isbalenced = False
            
            return 1 + max(lh, rh)

        find_height(root)

        return self.isbalenced


        