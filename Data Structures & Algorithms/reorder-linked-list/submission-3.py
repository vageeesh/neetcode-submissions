# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # idea, since i will be having only  pointer, use stack
        # traverse once, push and then keep on poping and assigning
        st = []
        tmp = head
        while tmp:
            st.append(tmp.val)
            tmp = tmp.next
        
        # keep on popping and assigning
        tmp_head = head
        i = 0
        l = len(st)

        if l > 2:

            while i < (l//2) :
                p = st.pop()
                new_node = ListNode(p)
                next_node = tmp_head.next

                # now change next node to new node created from stack
                tmp_head.next = new_node
                # new nodes next should be next node
                new_node.next = next_node

                # increment head
                tmp_head = next_node
                i += 1

            if l % 2 != 0:
                # odd length, so i have to attach the odd node for which there is not equvivilent n-1 node
                new_node.next = ListNode(st[i])
                new_node = new_node.next

            new_node.next = None

        