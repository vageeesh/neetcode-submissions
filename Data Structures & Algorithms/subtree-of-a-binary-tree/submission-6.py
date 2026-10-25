# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Most optimial solution O(n)

        def pot(root):
            if not root:
                return '#'

            return f"{root.val},{pot(root.left)},{pot(root.right)}"
        
        
        q1_s = pot(root)
        q2_s = pot(subRoot)

        if q2_s in q1_s:
            return True
        return False


        