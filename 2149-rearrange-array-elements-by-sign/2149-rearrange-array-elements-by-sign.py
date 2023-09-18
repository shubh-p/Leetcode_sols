class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans

        
        