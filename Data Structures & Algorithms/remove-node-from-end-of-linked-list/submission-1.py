# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # idea: if i found total length, then i can say whicch node to remove easily
        # by using length - n to be removed

        thead = head
        l = 0
        while thead:
            thead = thead.next
            l += 1

        rm = 0
        prev = None
        rm_head = head

        while rm_head:
            if rm == (l -n):
                # remove
                # if nor previous, then first element to be removed, so move head
                if not prev:
                    head = head.next
                else:
                    prev.next = rm_head.next
                break
            else:
                prev = rm_head
                rm_head = rm_head.next

            rm += 1

        return head

        