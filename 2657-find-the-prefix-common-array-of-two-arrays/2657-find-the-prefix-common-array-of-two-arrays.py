class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        #a=>+1
        #b=>-1
        n=len(A)
        s=0
        ans=[]
        count=[0]* (n+1)
        # print(count)
        for i in range(n):
            if count[A[i]]==-1:
                s+=1
            count[A[i]]+=1
            if count[B[i]]==1:
                s+=1
            count[B[i]]-=1
            ans.append(s)
        return ans