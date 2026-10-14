# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Idea: Check first node, which is lesser stat from that
        # after that keep on chekcing the next values between 2 lists
        # keep shifting to whichever is less, untill arrive end of both

        if not list1:
            return list2
        if not list2:
            return list1

        head1 = list1
        head2 = list2
        head = ListNode()
        tmp_head = head

        while head1 or head2:
            if not head1:
                while head2:
                    new_node=ListNode(head2.val)
                    tmp_head.next=new_node
                    tmp_head = new_node
                    head2 = head2.next
            if not head2:
                while head1:
                    new_node=ListNode(head1.val)
                    tmp_head.next=new_node
                    tmp_head = new_node
                    head1 = head1.next
            
            if head1 and head2:
                if head1.val < head2.val:
                    new_node=ListNode(head1.val)
                    tmp_head.next=new_node
                    head1 = head1.next
                    tmp_head = new_node
                else:
                    new_node=ListNode(head2.val)
                    tmp_head.next=new_node
                    head2 = head2.next
                    tmp_head = new_node

        return head.next


            


        