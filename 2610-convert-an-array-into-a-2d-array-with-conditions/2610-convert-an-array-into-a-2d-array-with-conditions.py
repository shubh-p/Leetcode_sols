class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        # print(count)
        ans=[]
        n,x=0,len(nums)
        while n<x:
            temp=[]
            for a in count:
                if count[a]>0:
                    temp.append(a)
                    count[a]-=1
                    n+=1
            ans.append(temp)
            
            
        return ans