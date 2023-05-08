class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        n=len(nums)
        for num in nums:
            a[num]= 1 + a.get(num,0) # number -> count
        z=n+1
        ans=[]
        b=[[] for j in range(z)]
        for x,y in a.items():
            b[y].append(x);          #count ->numbers
        for i in range(len(b)-1,0,-1):
            for n in b[i]:
                ans.append(n)
                if(len(ans)==k):
                    return ans
        
        return ans
        