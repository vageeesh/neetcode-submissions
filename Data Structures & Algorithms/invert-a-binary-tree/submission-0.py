# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        self.traverse(root.right)

        # invert here
        tmp = root.left
        root.left = root.right
        root.right = tmp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
        