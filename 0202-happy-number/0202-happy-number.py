class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n not in a:
            a.add(n)
            temp=n
            sum=0
            while temp!=0:
                dig=temp%10
                sum+=dig**2
                temp=temp//10
            n=sum
            if n==1:
                return True
        return False
            