# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_kth(self, head, k):
        while head and k > 0:
            head = head.next
            k -=1

        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy

        # find k nodes to be reversed in loop
        while True:
            kth = self.find_kth(previous, k)

            # if not enough elements then break
            if not kth:
                break

            nextgroup = kth.next
            # kth element present, now reverse between next to previous till k
            # or next to previuos and before nextgroup

            p = nextgroup
            current = previous.next

            while current != nextgroup:
                n = current.next
                current.next = p
                p = current
                current = n

            # now above logic would have reveresed k elements and 
            # also linked the right most next node to it

            # Taks: update previous and 
            # we have to link previous to start of this 'kth'
            # current previous have link to first element before reverse, i have to replace that and link to first element after reverse

            # this need because now this is reversed so next previous 
            # should start from here
            tmp = previous.next
            # since reversed, kth will come first element so, link to that
            previous.next = kth
            # next previous will be the last element of current batch(since reversed)
            previous = tmp

        return dummy.next

