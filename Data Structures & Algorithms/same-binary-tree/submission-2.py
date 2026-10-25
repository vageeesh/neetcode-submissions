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
            if not p and not q:
                return True
            else:
                if not p or not q:
                    return False

            
            if p.val!=q.val:
                return False


            lv = check_same(p.left, q.left)
            rv = check_same(p.right, q.right)

            return lv and rv
            

        v = check_same(p, q)
        return v
        