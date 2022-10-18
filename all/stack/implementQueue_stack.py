class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):   
            for i in range(len(self.stack)):
                self.stack2.append(self.stack.pop())
            removedItem = self.stack2.pop()
            for i in range(len(self.stack2)):
                self.stack.append(self.stack2.pop())
            return removedItem

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
