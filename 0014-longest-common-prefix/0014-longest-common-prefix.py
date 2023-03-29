class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        ans=""
        j=0
        while j<len(strs[0]):
            #print(1)
            c=strs[0][j]
            for word in strs:
                if j>=len(word) or word[j]!=c:
                    #print(2)
                    return ans
            #print(word,word[j])
            #print(3)
            ans+=word[j]
            j+=1
        return ans
                
        