class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num=n
        ans=[]
        while num:
            ans.append(num%k)
            num=num//k
        #print(ans)
        return sum(ans)