# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # To reduce time we have to do 2 things:
        # 1. dont find index array but create dict
        # 2. dont slice array which is O(N**2) but just keep pointers

        self.iorderindex_map = {}
        for i, each in enumerate(inorder):
            self.iorderindex_map[each] = i
        
        self.preorder = preorder
        self.inorder = inorder

        
        def ctree_dfs(pre_start, pre_end, in_start, in_end):
            if (pre_start > pre_end) or (in_start > in_end):
                return

            # first element
            root = TreeNode(self.preorder[pre_start])

            # find mid in inorder
            mid = self.iorderindex_map[root.val]

            left_size = mid - in_start

            root.left = ctree_dfs(pre_start+1, pre_start+left_size, in_start, mid-1)
            root.right = ctree_dfs(pre_start+left_size+1, pre_end, mid+1, in_end)

            return root


        return ctree_dfs(0, len(preorder)-1, 0, len(inorder)-1)

        