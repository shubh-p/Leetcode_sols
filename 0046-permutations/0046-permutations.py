class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def rec(op,ip):
            if len(ip)==0:
                nonlocal ans
                ans.append(op)
            for i in range(len(ip)):
                nop=op.copy()
                nop.append(ip[i])
                nip=ip.copy()
                nip.remove(ip[i])
                rec(nop,nip)
        
        rec([],nums)
        return ans