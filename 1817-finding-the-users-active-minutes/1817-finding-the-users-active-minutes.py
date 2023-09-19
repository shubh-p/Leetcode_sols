class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        occured=set()
        count={}
        for log in logs:
            if tuple(log) not in occured:
                occured.add(tuple(log))
                count[log[0]]=count.get(log[0],0)+1
        # print(count)
        ans=[0 for i in range(k)]
        for value in count.values():
            ans[value-1]+=1
        return ans
        