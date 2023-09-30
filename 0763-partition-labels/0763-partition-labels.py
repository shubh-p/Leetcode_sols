class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in dic:
                dic[s[i]]=i
        # print(dic)
        ans=[]
        def rec(start,c):
            last=dic[c]
            for i in range(start,last+1):
                if dic[s[i]]>last:
                    last=rec(i,s[i])
            return last
        sol=[]
        j,sum=0,0
        while j <len(s):
            ans=rec(j,s[j])
            sol.append(ans+1-sum)
            sum+=ans+1-sum
            j=ans+1
        return sol