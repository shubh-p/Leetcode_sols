class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a={}
        for i,num in enumerate(nums):
            if num in a:
                a[num].append(i)
            else:
                a[num]=[i]
       #print(a.values())
        for pos in a.values():
            if len(pos)>1:
                for i in range(len(pos)-1):
                    if abs(pos[i]-pos[i+1])<=k:
                        return True
        return False
            