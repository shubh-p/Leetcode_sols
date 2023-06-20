class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def fn(Type):
            total=0
            curr=0
            for number,house in enumerate(garbage):
                times=house.count(Type)
                if times!=0:
                    distance=sum(travel[curr:number])
                    total+=distance
                    curr=number
                    total+=times
            return total
        ans=fn('G')+fn('P')+fn('M')
        return ans
                        