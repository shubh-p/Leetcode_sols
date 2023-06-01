class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op=[]
        ans=[]
        def rec(op,ip):
            if len(ip)==0:
                ans.append(op)
                return
            last=ip.pop()
            # print(op,ip,last)
            rec(op,ip)
            # print(op,ip,last)
            rec(op+[last],ip)
            ip.append(last)
        
        rec(op,nums)
        return ans
            