class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1] <= val:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]
            del self.min_stack[-1]
        else:
            return 'Empty stack'

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return 0
        else:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()