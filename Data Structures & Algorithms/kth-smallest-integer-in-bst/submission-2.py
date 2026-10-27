# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # idea: we know left will have minimum and right max
        # so using in-order traversal and counting, we can find
        self.count = 0
        self.res = None

        def inordert(root, k):
            if not root:
                return

            l = inordert(root.left, k)
            self.count += 1
            if self.count == k and self.res is None:
                self.res = root.val
                return
            r = inordert(root.right, k)

        
        inordert(root, k)
        return self.res
            
            

        