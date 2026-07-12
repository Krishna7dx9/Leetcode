class MinStack(object):

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val):
        self.data.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self):
        self.data.pop()
        self.min_stack.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()