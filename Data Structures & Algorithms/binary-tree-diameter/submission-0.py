# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # algoritham: at each node find the ledt height + right height
        # and max of sunch heights is the answer
        # lets use dfs
        self.dia = 0

        def cal_h(root):
            if not root:
                return 0
            
            left_h = cal_h(root.left)
            right_h = cal_h(root.right)

            self.dia = max(self.dia, (left_h + right_h))

            return 1 + max(left_h, right_h)

        cal_h(root)

        return self.dia
        

