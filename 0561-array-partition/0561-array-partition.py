class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        count=[0]*(2*(10**4) + 1)
        for i in nums:
            count[i+10000]+=1
        for j in range(1,len(count)):
            count[j]+=count[j-1]
        ans=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            count[nums[i]+10000]-=1
            ans[count[nums[i]+10000]]=nums[i]
        print(ans)
        s=0
        for i,a in enumerate(ans):
            if i%2==0:
                s+=a
        return s