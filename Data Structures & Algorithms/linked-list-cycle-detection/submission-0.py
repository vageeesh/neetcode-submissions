# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        tmp=head
        circ=False
        while tmp:
            if id(tmp) in visited:
                circ=True
                break
            else:
                visited.add(id(tmp))
            
            tmp=tmp.next
            


        return circ
        