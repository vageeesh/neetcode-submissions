# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # without using extra space
        # idea: devide into 2 half, reverse the second part
        # then merge both the parts

        # 1. devide into 2 halfs
        sl = head
        fst = head.next
        while fst and fst.next:
            # by end of this, i will have 2 half
            # end of sl will be first half
            sl = sl.next
            # move fast by 2 pointers
            fst = fst.next.next

        sc_half = sl.next
        # close first half
        sl.next = None

        # now step 2: reverse the second part
        prev = None
        while sc_half:
            tmp_n = sc_half.next
            sc_half.next = prev
            prev = sc_half
            sc_half = tmp_n

        # step 3: merge these 2 now:
        # we know that second half will be shorter[in case of odd numbers]
        # so keep loop till secondhalf exists
        first_half = head
        # it should be previous because sc_half became NULL above, so previous will hold last val
        sc_half = prev
        while sc_half:
            # store fist and second next values
            tmp1 = first_half.next
            tmp2 = sc_half.next

            first_half.next = sc_half
            sc_half.next = tmp1

            first_half = tmp1
            sc_half = tmp2



        