class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy head/tail banate hain edge cases handle karne ke liye
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # head ke paas (most recent), tail ke paas (least recent)
    
    def _remove(self, node):
        # node ko list se nikaal do
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        # node ko head ke turant baad daalo (most recently used)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Is node ko use kiya gaya hai, isliye ise "recently used" mark karo:
        self._remove(node)  # purani position se hatao
        self._add_to_front(node) # Nya position pe add kro
        return node.val

    def put(self, key: int, value: int) -> None:
        # Agar key pehle se cache mein hai, toh purana node hatao
        # (kyunki hum naya node banayenge same key ke liye)
        if key in self.cache:
            self._remove(self.cache[key])

        # Naya node banao is key-value ke saath
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        # Agar capacity se zyada ho gaya, toh sabse purana (LRU) node hatao
        if len(self.cache) > self.capacity:
            # tail ke pehle wala node hatao (LRU) = least recently used
            lru = self.tail.prev
            self._remove(lru)  # linked_list se htao
            del self.cache[lru.key]  # hashmap se hataya

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)