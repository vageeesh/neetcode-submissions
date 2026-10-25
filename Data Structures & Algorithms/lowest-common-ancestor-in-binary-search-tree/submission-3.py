# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this should never hit, but to avoid Null errors
        if not root:
            return
        
        # reverse
        if p.val > q.val:
            p, q = q, p
        
        if (p.val < root.val and q.val > root.val):
            return root
        elif (p.val == root.val) and (q.val > root.val):
            return root
        elif q.val == root.val and (p.val < root.val):
            return root

        if p.val < root.val and q.val < root.val:
            # move left sub-tree
            v = self.lowestCommonAncestor(root.left, p, q)
        else:
            # move right
            v = self.lowestCommonAncestor(root.right, p, q)

        return v

        
        


        