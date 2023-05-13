class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[None] * k
        self.head=-1
        self.tail=-1
        self.max=k
        #print(self.head,self.tail)

    def enQueue(self, value: int) -> bool:
        if self.isFull()==True:
            return False
        elif self.isEmpty()==True:
            self.head,self.tail=0,0
        else:
            if self.tail==self.max-1:
                self.tail=0
            else:
                self.tail+=1
        self.queue[self.tail]=value
        #print(self.queue,self.head,self.tail)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty()==True:
            return False
        self.queue[self.head]=None
        if self.isOne()==True:
            self.head,self.tail=-1,-1
        elif self.head==self.max-1:
            self.head=0
        else:
            self.head+=1
        #print(self.queue,self.head,self.tail)
        return True

    def Front(self) -> int:
        if self.isEmpty()==True:
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty()==True:
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head==-1 and self.tail==-1:
            #print("Empty")
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if self.head==0 and self.tail==self.max-1:
            #print("Empty")
            return True
        elif self.head==self.tail+1:
            #print("Empty")
            return True
        else:
            return False
    def isOne(self) -> bool:
        if self.head==self.tail and self.head!=-1:
            #print("Single")
            return True
        else:
            return False
            


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()