class MyQueue:

    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]

    def push(self, x: int) -> None:
        while len(self.pop_stack)>0:
            a=self.pop_stack.pop(-1)
            self.push_stack.append(a)
        self.push_stack.append(x)

    def pop(self) -> int:
        while len(self.push_stack)>0:
            a=self.push_stack.pop(-1)
            self.pop_stack.append(a)
        res=self.pop_stack.pop(-1)
        return res
    def peek(self) -> int:
        while len(self.push_stack)>0:
            a=self.push_stack.pop(-1)
            self.pop_stack.append(a)
        res=self.pop_stack[-1]
        return res

    def empty(self) -> bool:
        if len(self.push_stack)==0 and len(self.pop_stack)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()