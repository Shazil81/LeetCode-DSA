class MyStack:
    # implenting using 2 queues 
    def __init__(self):
       self.q1 = deque()
       self.q2 = deque() 

    def push(self, x: int) -> None:
        # Add new to helper
        self.q2.append(x)
        # Move all from main to helper
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap helper becomes main
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        
        return self.q1.popleft() # popleft is liye kyun ki last element whi pe hoga

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()