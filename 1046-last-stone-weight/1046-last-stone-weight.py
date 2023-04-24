class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            f,s=-1,-1
            i,j=-1,-1
            for pos in range(len(stones)):
                if stones[pos]>f:
                    s=f
                    f=stones[pos]
                    j=i
                    i=pos
                elif stones[pos]>s:
                    s=stones[pos]
                    j=pos
            stones[i]=stones[i]-stones[j]
            stones.remove(stones[j])
        if len(stones):
            return stones[0]
        else:
            return 0
            
                    
            