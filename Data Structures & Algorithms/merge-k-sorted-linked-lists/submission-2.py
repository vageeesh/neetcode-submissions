# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def sortlist(self, l1, l2):
        self.dum = ListNode()
        tmp = self.dum

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next

            tmp = tmp.next

        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2

        return self.dum.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # optimal solution:
        # use merge sort concept: take 2 list at once merge, and keep on doing it until nothing left
        # this will keep time complexity in O(N⋅klogN)

        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                merged_list.append(self.sortlist(l1, l2))
            
            lists = merged_list

        return lists[0]

