# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def traverse_tree(self, root, q):
        if not root:
            return None

        # pre-order traversal:
        q.append(root.val)
        q.append(self.traverse_tree(root.left, q))
        q.append(self.traverse_tree(root.right, q))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # easy way i can think quickly is traverse with same order and check if they are same
        self.traverse_tree(p, self.q1)
        self.traverse_tree(q, self.q2)

        if self.q1 == self.q2:
            return True

        return False
        