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

        def inordert(root, k):
            if not root:
                return

            l = inordert(root.left, k)
            # return for left side search
            if l is not None:
                return l

            self.count += 1
            if self.count == k:
                # will be returned to eitherr right or left
                return root.val

            # return for right side search
            return inordert(root.right, k)


        v = inordert(root, k)
        return v
            
            

        