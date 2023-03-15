class Solution:
    def countPoints(self, rings: str) -> int:
        ans=defaultdict(set)
        for i,c in enumerate(rings):
            if i%2==0:
                color=c
            else:
                ring=c
                ans[ring].add(color)
        count=0
        for v in ans.values():
            print(v)
            if v == {'G','B','R'}:
                count+=1
        return count
            
