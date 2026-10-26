# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Idea, use BFS: And always print/get only last element (right side) in Q
        if not root:
            return []

        from collections import deque
        q = deque()
        q.append(root)
        res = []

        while q:
            for i in range(len(q)):
                p = q.popleft()
                if p.left:
                    q.append(p.left)
                
                if p.right:
                    q.append(p.right)

            res.append(p.val)

        return res
        