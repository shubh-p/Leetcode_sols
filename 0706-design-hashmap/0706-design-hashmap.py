class MyHashMap:
        def __init__(self):
            self.size=1000000
            self.table=[None]*self.size
        def hashv(self,key:int)->int:
            return key%self.size
        def put(self, key: int, value: int) -> None:
            hv=self.hashv(key)
            self.table[hv]=[key,value]
        def get(self, key: int) -> int:
            hv=self.hashv(key)
            ans=self.table[hv]
            if ans==None:
                return -1
            else:
                return ans[1]
            #print(type(ans))
        def remove(self, key: int) -> None:
            hv=self.hashv(key)
            self.table[hv]=None


    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)