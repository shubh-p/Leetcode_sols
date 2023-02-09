class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        same=[]
        more=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                same.append(i)
            else:
                more.append(i)
        return less+same+more
        