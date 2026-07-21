class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        s = Node(key, value)
        if key not in self.cache:
            if len(self.cache) >= self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                self.cache[key] = s
                self.insert(s)
            else:
                self.cache[key] = s
                self.insert(s)
        else:
            self.remove(self.cache[key])
            self.insert(s)
            self.cache[key] = s

        
