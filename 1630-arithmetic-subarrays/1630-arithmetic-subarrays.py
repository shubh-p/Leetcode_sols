class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m=len(l)
        n=len(nums)
        ans=[]
        for i in range(m):
            temp=nums[l[i]:r[i]+1]
            temp.sort()
            flag=1
            for i in range(2,len(temp)):
                if temp[i]-temp[i-1]!=temp[1]-temp[0]:
                    ans.append(False)
                    flag=0
                    break
            # print(temp,flag)
            if flag==1:
                ans.append(True)
        return ans
