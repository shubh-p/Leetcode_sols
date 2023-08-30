class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (x[1]),reverse=True)
        totalboxes,totalunits=0,0
        for boxes in boxTypes:
            n,units=boxes[0],boxes[1]
            space=truckSize-totalboxes
            if space>n:
                totalboxes+=n
                totalunits+=(n*units)
            elif space>0:
                totalboxes+=space
                totalunits+=(space*units)
            else:
                return totalunits
        return totalunits