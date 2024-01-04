class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def rec(n):
            if n==1:
                return -1
            elif n<=3:
                return 1
            elif n==4:
                return 2
            else:
                return 1 + rec(n-3)
        count=Counter(nums)
        ans,temp=0,0
        for _ in count.values():
            temp=rec(_)
            if temp==-1:
                return -1
            else:
                ans+=temp
        return ans