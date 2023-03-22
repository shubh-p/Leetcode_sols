class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        x=bin(n)
        length=len(x)
        even=True
        odd=False
        e,o=0,0
        for i in range(length-1,1,-1):
            #print(x[i])
            if even:
                if x[i]=="1":
                    e+=1
                even=False
                odd=True
            elif odd:
                if x[i]=="1":
                    o+=1
                odd=False
                even=True
        return[e,o]