class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            temp=i
            flag=1
            if temp>9:
                while temp!=0:
                    digit=temp%10
                    if digit==0:
                        flag=0
                        break
                    if i%digit!=0:
                        flag=0
                        break
                    temp=int(temp/10)
            if flag==1:
                ans.append(i)
        return ans