class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat[0])
        ans=[]
        for i in mat:
            ans.append(sum(i))
        print(ans)
        print(n)
        sol=[]
        count=0
        m=n+1
        while count<k:
            m=n+1
            for i in range(len(ans)):
                if ans[i]<m:
                    m=ans[i]
                    pos=i
            sol.append(pos)
            ans[pos]=n+1
            count+=1
        return sol
            
            