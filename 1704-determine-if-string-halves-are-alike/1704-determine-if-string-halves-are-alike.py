class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        a=s[0:int(n/2)]
        b=s[int(n/2):n]
        ca,cb=0,0
        print(a,b)
        for i in a:
            if i in ['a','e','i','o','u']:
                ca+=1
        for i in b:
            if i in ['a','e','i','o','u']:
                cb+=1
        return ca==cb