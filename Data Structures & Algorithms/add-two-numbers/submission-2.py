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
        while l1 and l2:
            res = (l1.val + l2.val + car)

            if res > 9:
                res = res % 10
                car = 1
            else:
                car = 0
                
            dum.next = ListNode(res)
            dum = dum.next

            l1 = l1.next
            l2 = l2.next

        leftover_nodes = l1 if l1 else l2
        while leftover_nodes:
            res = (leftover_nodes.val + car)
            if res > 9:
                res = res % 10
                car = 1
            else:
                car = 0
            dum.next = ListNode(res)
            dum = dum.next
            leftover_nodes = leftover_nodes.next

        if car:
            dum.next = ListNode(car)

        return head.next

        