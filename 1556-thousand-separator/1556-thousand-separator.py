class Solution:
    def thousandSeparator(self, n: int) -> str:
        num=list(str(n))
        if len(num)<4:
            return "".join(num)
        count=1
        for i in range(len(num)-1,-1,-1):
            if count%3==0 and count!=0:
                num.insert(i,".")
            count+=1
        if num[0]==".":
            num=num[1:]
        return "".join(num)