class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def fn(n,k):
            if k==1 and n==1:
                return 0
            if k==1 and n==2:
                return 0
            if k==2 and n==2:
                return 1
            temp=2**(n-1)
            if k<=temp/2:
                return fn(n-1,k)
            elif k<=temp*3/4:
                return fn(n-2,k-temp/2)^1
            else:
                return fn(n-2,k-temp*3/4)
            
        return fn(n,k)
            