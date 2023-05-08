class RandomizedSet:
    a=[]
    count=0
    pos={}
    def __init__(self):
        self.a=[]
        self.count=0
        self.pos={}
    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        else:
            self.a.append(val)
            self.pos[val]=self. count
            self.count+=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.a:
            self.a[self.pos[val]]=self.a[self.count-1]
            self.pos[self.a[self.count-1]]=self.pos[val]
            self.a.pop()
            self.count-=1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.a[random.randint(0, self.count - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()