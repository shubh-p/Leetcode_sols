class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max1,max2,count1,count2=0,1,0,0
        for num in nums:
            if num==max1:
                count1+=1
            elif num==max2:
                count2+=1
            elif count1==0:
                count1=1
                max1=num
            elif count2==0:
                count2=1
                max2=num
            else:
                count1-=1
                count2-=1
        ans=[]
        n=len(nums)
        if nums.count(max1)>n//3:
            ans.append(max1)
        if nums.count(max2)>n//3:
            ans.append(max2)
        return ans
           