class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.n = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # dict with key and val as node itself, so we can do all operation in O(1)
        self.mapp = {}
        self.max_cap = capacity
        self.cu_cap = 0
        self.left, self.right = Node(0,0),  Node(0,0)
        self.left.n = self.right
        self.right.prev = self.left

    def delete(self, node):
        prev, nex = node.prev, node.n
        # update previsous next and next's previous, current will be removed
        prev.n = nex
        nex.prev = prev

    def insert(self, node):
        # insert is always at the end
        # right pointer (dummy) will be end, so i will insert just before that
        prev, nex = self.right.prev, self.right
        node.prev = prev
        node.n = nex
        prev.n = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.mapp:
            # move that node to end(recently accessed to right most)
            self.delete(self.mapp[key])
            self.insert(self.mapp[key])
            return self.mapp[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            # already present, delete from that position and move to end
            self.delete(self.mapp[key])
            self.insert(self.mapp[key])
            # update new value for node
            self.mapp[key].val = value
        else:
            self.cu_cap += 1
            # create new and insert at end
            new_node = Node(key, value)
            self.mapp[key] = new_node
            self.insert(self.mapp[key])

            # check if capacity is full:
            if self.cu_cap > self.max_cap:
                # already full, so deleet least used which is left most
                # left is dummy, so next of left to delete
                # delete from dict
                del self.mapp[self.left.n.key]
                self.delete(self.left.n)
                

        
