class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count=Counter(tasks)
        ans=0
        for i in count.values():
            if i==1:
                return -1
            rem=i%3
            if rem==0:
                ans+=i//3
            else:
                ans+=(i+3-rem)//3
        return ans