class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for j in range(len(strs[0])):
            temp=""
            for i in range(len(strs)):
                temp+=strs[i][j]
            k=sorted(temp)
            if list(temp)!=k:
                count+=1
        return count