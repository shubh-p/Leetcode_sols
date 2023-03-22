class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0":
            return b
        if b=="0":
            return a
        m=len(a)
        n=len(b)
        x=list(a)
        y=list(b)
        ans=""
        length=m
        if m>n:
            y=[0]*(m-n)+y
            length=m
        elif n>m:
            x=[0]*(n-m)+x
            length=n
        #print(x,y)
        carry=0
        for i in range(length-1,-1,-1):
            if int(x[i])+int(y[i])+carry==2:
                ans+="0"
                carry=1
            elif int(x[i])+int(y[i])+carry==3:
                ans+="1"
                carry=1
            elif int(x[i])+int(y[i])+carry==1:
                ans+="1"
                carry=0
            else:
                ans+="0"
                carry=0
        if carry==1:
            ans+="1"
        return ans[::-1]
                
        
