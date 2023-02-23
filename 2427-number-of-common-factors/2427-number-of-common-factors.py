class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n=min(a,b)
        sum=0
        for i in range(1,n+1):
            #print(i)
            if a%i==0 and b%i==0:
                sum+=1
        return sum
            