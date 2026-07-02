class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val, val]) # double element is liye ki ek min hoga or ek val baar baar update jayega
        else:
            # yha pe min val update ho ja rha h
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()