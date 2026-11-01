# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def preorder(self, root):
        st = []

        def traverse(root):
            if not root:
                st.append('None')
                return

            st.append(str(root.val))
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return st
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # idea covert inorder and preorder seperated by |
        # so in decode also we can do the same
        st = self.preorder(root)
        return ','.join(st)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        self.index = 0
        
        # now recursively do 
        def construct_tree(li):
            if (li[self.index] == 'None'):
                self.index += 1
                return

            root = TreeNode(li[self.index])

            self.index += 1
            
            root.left = construct_tree(li)
            root.right = construct_tree(li)

            return root

        return construct_tree(res)
        
            
