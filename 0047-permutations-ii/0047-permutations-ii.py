class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def rec(op,ip):
            nonlocal ans
            if len(ip)==0 :
                ans.append(op)
            
            for i in range(len(ip)):
                if i>0 and ip[i]==ip[i-1]:
                    continue
                nop=op.copy()
                nop.append(ip[i])
                nip=ip.copy()
                nip.remove(ip[i])
                rec(nop,nip)
                
        rec([],nums)
        return ans