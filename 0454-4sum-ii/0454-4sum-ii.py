class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums={}
        ans=0
        for x in nums1:
            for y in nums2:
                sums[x+y]=sums.get(x+y,0)+1
        for a in nums3:
            for b in nums4:
                req=-1*(a+b)
                if req in sums:
                    ans+=sums[req]
        return ans