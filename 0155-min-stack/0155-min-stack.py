class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))
        # print('push',self.stack)
    def pop(self) -> None:
        self.stack.pop(-1)
        # print('pop',self.stack)
    def top(self) -> int:
        # print('top',self.stack)
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        # print('min',self.stack)
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()