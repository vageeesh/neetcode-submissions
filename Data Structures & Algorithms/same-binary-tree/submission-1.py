# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_same = True

        def check_same(p, q):
            if not p or not q:
                if p and not q:
                    self.is_same = False
                if q and not p:
                    self.is_same = False
                return
            
            if p.val!=q.val:
                self.is_same = False
            
            check_same(p.left, q.left)
            check_same(p.right, q.right)
            

        check_same(p, q)
        return self.is_same
        