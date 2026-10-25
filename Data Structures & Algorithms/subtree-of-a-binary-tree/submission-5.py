# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_same(self, t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            
            return self.check_same(t1.left, t2.left) and self.check_same(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # i have to check if its same at each node
        if not root:
            return False

        # tarverse, no need to check if root and subroot val is same 
        # and then only start becaue that is handled in check_same
        if self.check_same(root, subRoot):
            return True

        # # tarverse
        # if root.val == subRoot.val:
        #     # check if they are same
        #     is_sub_tree = self.check_same(root, subRoot)
        #     if is_sub_tree:
        #         return True

        # # traverse left and check
        # l = self.isSubtree(root.left, subRoot)
        # r = self.isSubtree(root.right, subRoot)
        # return l or r

        # above commmented code is wrong way of writig code
        # because i have l or r so with above it will process both the sides always
        # with below code if left is True then it will Skip right side execution so very optimal and rec. way to use(This is always sequential)

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        