# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # i have to keep track of both min and max so that
        # everywhere downstream it should be same
        # import float
        leftb = float("-inf")
        rightb = float("inf")
        
        def checkbtree(root, left_b, right_b):
            if not root:
                return True
            
            if not (left_b < root.val < right_b):
                return False

            l = checkbtree(root.left, left_b, root.val)
            r = checkbtree(root.right, root.val, right_b)

            return (l and r)

        return checkbtree(root, leftb, rightb)

        