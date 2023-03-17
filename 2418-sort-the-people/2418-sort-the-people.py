class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a={}
        for i in range(len(names)):
            a[heights[i]]=names[i]
        ans=sorted(a.items())
        print(ans)
        anss=[]
        for i in ans:
            anss.append(i[1])
        anss.reverse()
        return anss    