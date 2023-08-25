class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans=[]
        nums=[i for i in range(1,n+1)]
        def rec(op,ip):
            nonlocal ans
            if len(op)==k:
                ans.append(op)
            for i in range(len(ip)):
                nop=op.copy()
                nop.append(ip[i])
                nip=ip[i+1:]
                rec(nop,nip)
        
        rec([],nums)
        return ans