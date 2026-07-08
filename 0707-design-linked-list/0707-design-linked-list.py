class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = Node(0) # dummy Node bnaye taaki asaani ho
        self.size = 0  # size lene se bhi asaani ho rhi h
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        self.size+=1
        curr = self.head
        for _ in range(index):
            curr = curr.next
            
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size-=1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)