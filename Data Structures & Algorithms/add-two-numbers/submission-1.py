# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dum = ListNode(0)
        head = dum
        car = 0
        while l1 or l2:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val

            res = (l1_val + l2_val + car)

            if res > 9:
                res = res % 10
                car = 1
            else:
                car = 0
                
            dum.next = ListNode(res)
            dum = dum.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if car:
            dum.next = ListNode(car)

        return head.next

        