# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # simple idea with extra space is inorder traversal
        # and then check if its sorted
        self.q = []

        def inordertraversal(root):
            if not root:
                return

            inordertraversal(root.left)
            self.q.append(root.val)
            inordertraversal(root.right)

        if not root:
            return True

        inordertraversal(root)

        for i in range(len(self.q)-1):
            if self.q[i] >= self.q[i+1]:
                return False
        return True
