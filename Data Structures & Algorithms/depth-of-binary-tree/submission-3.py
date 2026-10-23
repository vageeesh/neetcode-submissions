# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # solving using DFS but iterative and not recurssive
        if not root:
            return 0

        st = []
        max_depth = 0
        # without depth, i will not be able to find the depth, so keep depth as well in stack
        st.append([root, 1])
        while st:
            p = st.pop()
            # append right first then left because i have to process left nodes first,
            # so last append will get processed first
            if p[0]:
                max_depth = max(max_depth, p[1])
                st.append([p[0].right, 1 + p[1]])
                st.append([p[0].left, 1 + p[1]])

        return max_depth

