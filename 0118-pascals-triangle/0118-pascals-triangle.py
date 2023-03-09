class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fact(num:int) -> int:
            x=1
            for i in range(1,num+1):
                x*=i
            return x
        ans=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(int(fact(i)/(fact(j)*fact(i-j))))
            ans.append(temp)
            
        return ans
            