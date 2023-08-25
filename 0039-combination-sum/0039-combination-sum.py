class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        comb=[]
        def rec(comn,tofind,candi):
            if tofind==0:
                ans.append(comb[:])
            for i in range(len(candi)):
                if candi[i]<=tofind:
                    tofind-=candi[i]
                    comb.append(candi[i])
                    rec(comb,tofind,candi[i:])
                    comb.pop()
                    tofind+=candi[i]
        rec([],target,candidates)
        return ans
