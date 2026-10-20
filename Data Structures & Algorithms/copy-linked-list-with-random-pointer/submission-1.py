"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # i struggled here, i had idea of using map but i was keeping 2 dict 1 to keep randome val and another to keep nodes itself, later in second pass trying to link randome value to random node
        # i was wrong, right way to do it is just map between old and new node, thats it
        node_map = {}
        # step 1: create node and mapping
        tmp = head
        while tmp:
            new_node = Node(tmp.val)
            node_map[tmp] = new_node
            tmp = tmp.next
        
        # step 2: just link both next and random using dict/map
        tmp = head
        while tmp:
            node_map[tmp].next = node_map.get(tmp.next, None)
            node_map[tmp].random = node_map.get(tmp.random, None)

            tmp = tmp.next

        return node_map.get(head, None)