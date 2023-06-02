class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        # print(a)
        def rec(a,start):
            if len(a)==1:
                return a[0]
            index=(start+k-1)%len(a)
            a.pop(index)
            return rec(a,index)
            
        return rec(a,0)