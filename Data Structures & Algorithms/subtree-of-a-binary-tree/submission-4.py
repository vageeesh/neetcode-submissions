# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Most optimial solution O(n)
        self.q1 = []
        self.q2 = []

        def pot(root):
            if not root:
                return '#'

            self.q1.append(str(root.val))

            self.q1.append(pot(root.left))
            self.q1.append(pot(root.right))
            return ('_')
        
        def subpot(sub_root):
            if not sub_root:
                return '#'

            self.q2.append(str(sub_root.val))
            self.q2.append(subpot(sub_root.left))
            self.q2.append(subpot(sub_root.right))

            return ('_')
        
        pot(root)
        subpot(subRoot)

        # convert to string
        q1_s = ''.join(self.q1)
        q2_s = ''.join(self.q2)

        if q2_s in q1_s:
            return True
        return False


        