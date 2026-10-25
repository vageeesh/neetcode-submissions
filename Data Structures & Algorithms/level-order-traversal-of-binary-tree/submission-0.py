# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # lets use BFS
        from collections import deque

        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            # since all nodes in that level to be appended at once
            # using loop: because all elements in queue at 1 point will be of same lev
            inner_lis = []
            for i in range(len(q)):
                node = q.popleft()
                inner_lis.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(inner_lis)

        return res
        