class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        spaces=[]
        for i in range(len(capacity)):
            spaces.append(capacity[i]-rocks[i])
        spaces.sort()
        # print(spaces)  
        for i,space in enumerate(spaces):
            if additionalRocks==0:
                break
            if space>0 and space<=additionalRocks:
                spaces[i]=0
                additionalRocks-=space
        # print(spaces)  
        return spaces.count(0)