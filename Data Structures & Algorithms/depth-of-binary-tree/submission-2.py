# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # let me solve using BFS method - Queue
        from collections import deque
        d = deque()

        if not root:
            return 0
        
        d.append(root)
        max_depth = 0

        while d:
            for i in range(len(d)):
                p = d.popleft()
                if p.left:
                    d.append(p.left)
                if p.right:
                    d.append(p.right)

            max_depth += 1
        
        return max_depth


